import requests
import pytest


class JK(object):
    def __init__(self):
        self.disable_url = "http://localhost:8080/job/PythonRun/disable"
        self.enable_url = "http://localhost:8080/job/PythonRun/enable"
        self.job_url = "http://localhost:8080/job/PythonRun/api/json"


class TestJenkins(object):
    """
    Test get a list of jobs from jenkins
    """
    @pytest.fixture(scope="module")
    def jk(self):
        return JK()

    def test_disable_job(self, jk):
        r = requests.post(jk.enable_url)
        assert r.status_code == 200
        requests.post(jk.disable_url)
        r = requests.get(jk.job_url)
        buildable = r.json()['buildable']
        assert buildable is False

    def test_enable_job(self, jk):
        r = requests.post(jk.disable_url)
        assert r.status_code == 200
        requests.post(jk.enable_url)
        r = requests.get(jk.job_url)
        buildable = r.json()['buildable']
        assert buildable is True


        