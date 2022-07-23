public class TaskLoopFour{
    public static void main(String[] args){
        int number=100;
        for(int j=2;j<=number;j++){
            boolean x= false; //标签初始态 
            //拍断j变量存储的数是否为素数                      
            for(int i=2;i<=j-1;i++){//剔除1和j存储数本身，用j存储的数分别除以把剩下的数
                if(j%i==0){//j存储的数分别除以把剩下的数
                    System.out.println(j+"不是素数");//其中有被整除的情况则if判断为true，当前j存储的数不为素数
                    x=true;//标签变化后状态（if判断为true）
                    break;//(中断当前循环)
                }        
            }
            if(x==false){
                System.out.println(j+"是素数");
            }            
        }        
    }
}
