import pytest
import time, json
import base64, hmac
import hashlib, uuid, re
import requests
import pandas as pd

# 先定义好conf配置代码
def config_txt(file_name="config.txt"):
    data_head = list()
    data_tail = list()
    for line in open(file_name, encoding='gb18030', errors='ignore'):
        head, sep, tail = line.partition('=')
        data_head.append(head.strip('\n '))
        if tail.find('#') != -1:
            tail, tail_b, tail_c = tail.partition('#')
        data_tail.append(tail.strip('\n  '))
    txt_data = dict(zip(data_head, data_tail))
    heada, sepa, taila = txt_data["GATEWAY_URL"].partition('/test_a')
    txt_data['HTTP_URI'] = "/test_a" + taila
    return txt_data

# conf文件配置样例:
GATEWAY_URL = https://127.0.0.1:8051/test_a/adk #url链接地址
zhu_KEY = test_key  #用户信息1
zhu_SECRET = test_secret #用户2
zhu_ID = 18825176013    #用户ID
zhuLY_ID = 588347220  #用户信息3

# 简单处理一下加密的处理，给后续持续调用
def md5(data_md5):
    data_md5 = hashlib.md5(data_md5.encode(encoding='UTF-8')).hexdigest()
    return data_md5

def sha256(data_sha256):
    data_sha256 = hashlib.sha256(data_sha256.encode(encoding='UTF-8')).hexdigest()
    return data_sha256

def hash_hmac(app_secret, msg, sha1):
    hmac_code = hmac.new(app_secret.encode(), msg.encode(), sha1).digest()
    return base64.b64encode(hmac_code).decode()

# 处理用例里面的加密变量,例如:请求参数md5(18812345678)先进行数据预处理
def body_encrypt(data_encrypt):
    if data_encrypt.find("sha256(") != -1:
        sha_ss = re.findall(r"sha256[(](.+?)[)]", data_encrypt)
        for i in range(len(sha_ss)):
            data_encrypt = re.compile("sha256[(]" + str(sha_ss[i]) + '[)]').sub(str(sha256(sha_ss[i])), data_encrypt)
    if data_encrypt.find("md5(") != -1:
        md5_ss = re.findall(r"md5[(](.+?)[)]", data_encrypt)
        for i in range(len(md5_ss)):
            data_encrypt = re.compile("md5[(]" + str(md5_ss[i]) + '[)]').sub(str(md5(md5_ss[i])), data_encrypt)
    return data_encrypt

# 读取excel文档里面的用例数据做为测试场景
def excel_case(file_name="case_file2.xlsx", case_id="all"):  # 读取excel账号及路由代理信息file_name
    data_excle = pd.read_excel(file_name, sheet_name=0, engine="openpyxl")
    df = pd.DataFrame(data_excle)
    if case_id != "all":
        df_data = df[(df.case_id == case_id)].to_dict('list')
    else:
        df_data = df.to_dict('list')
    case_id, case_name = df_data['case_id'], df_data['case_name']
    case_body, case_assert = df_data['case_body'], df_data['case_assert']
    case_body1 = body_encrypt(str(case_body))
    txt_data = list(zip(case_id, case_name, eval(case_body1), case_assert))
    return txt_data

# pytest的使用
class Test_zhu(object):
    #类初始化，此处在测试执行中，全局只会执行一次（读取配置文件）
    @classmethod
    def setup_class(self):
        self.text_data = config_txt()
   #方法初始化，此处在测试执行中，每条用例都会先执行一遍
    def setup_method(self):
        time.sleep(0.4)
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   #request接口请求的逻辑
    def request_id(self, GATEWAY_URL, http_body):
        HTTP_BODY = eval(http_body)
        TIME_STAMP = str(int((time.time() + 5) * 1000))
        zhuCE = uuid.uuid1().hex
        msg = self.text_data['zhuLY_ID'] + "\n" + TIME_STAMP + "\n" + zhuCE + "\n" + self.text_data['zhu_KEY'] + "\n" + \
              self.text_data["HTTP_URI"] + "\n" + json.dumps(HTTP_BODY)
        HTTP_HEADER = {
            "zhu_ID": self.text_data['zhu_ID'],
            "zhuLY_ID": self.text_data['zhuLY_ID'],
            "zhuCE": zhuCE,
            "zhu_KEY": self.text_data['zhu_KEY'],
            "TIMESTAMP": TIME_STAMP,
            "SIGNATURE": hash_hmac(self.text_data['zhu_SECRET'], msg, hashlib.sha1)}
        print('**请求参数:{}.'.format(HTTP_BODY))
        response_one = requests.post(GATEWAY_URL, json=HTTP_BODY, headers=HTTP_HEADER, verify=True)
        print('**响应结果:{}.'.format(response_one.text))
        return eval(response_one.text)
    #parametrize为数据驱动，此处获取了excle用例里的数据；apitest定个标签，后续冒烟啥的可以选择性的跑（暂时无用）；
    #excel_case(case_id="all")说明，all为全部用例执行或者指定用例执行case_0001
    @pytest.mark.parametrize('case_id,case_name, case_body, case_assert', excel_case(case_id="all"))
    @pytest.mark.apitest
    def test_zhu_case(self, case_id, case_name, case_body, case_assert):
        print("**\n执行编号：" + case_id + "\n**用例名称：" + case_name)
        case_assert_a = json.loads(case_assert)
        alertText = self.request_id(self.text_data['GATEWAY_URL'], case_body)
        retcode = case_assert_a.get('code') if case_assert_a.get('retcode') == None else case_assert_a.get('retcode')
        alertText_a = alertText.get('code') if alertText.get('retcode') == None else alertText.get('retcode')
        #此处为断言，判断用例通过还是不通过
        assert alertText_a == retcode

if __name__ == '__main__':
    pytest.main(["-sv", 'zhu_testA.py'])


# 利用pytest-html库可以生成html报告
# 命令：pytest zhu_testA.py --html=report.html --self-contained-html