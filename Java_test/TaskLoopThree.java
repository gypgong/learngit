//使用for循环打印九九乘法表
public class TaskLoopThree{
    public static void main(String[] args){
        int count=9;
        for(int i=1;i<=count;i++){
            //输出乘法等式+空格
            for(int j=1;j<=i;j++){
                System.out.print(j+"x"+i+"="+j*i+"\t");             
            }
        //换行
        System.out.println();
        }
    }
}