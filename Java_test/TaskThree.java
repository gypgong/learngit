//题目：求三位数字的水仙话数（153）

//方法一
/*
public class TaskThree{
    public static void main(String[] args){
        for(int num=100;num<=999;num++){
            int a = num/100;
            int b = num%100/10;
            int c = num%10;
            if(a*a*a + b*b*b + c*c*c == num){
                System.out.println(num);
            }
        }        
    }
}

*/
//方法二
public class TaskThree{
    public static void main(String[] args){
        //double value = Math.pow(double a,double b);//可即时a的b次方
        for(int num=100;num<=999;num++){
            /*int a = num/100;
            int b = num%100/10;//num/10%10
            int c = num%10;
            Math.pow(a,3)+ Math.pow(b,3) + Math.pow(c,3)*/
            if(Math.pow(num/100,3)+ Math.pow(num/10%10,3) + Math.pow(num%10,3) == num){
                System.out.println(num);
            }
        }        
    }
}