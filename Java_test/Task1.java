public class Task1{
    public static void main(String[] args){
        /*//排水问题
        int v = 120;
        int h = 0;
        while(v>0){
            v += 18;
            v -= 30;
            h ++;
            System.out.println("当前循环排水执行完毕:"+ v);
       }
       System.out.print("全部排完需要的时间："+h);
       */

       /*//画星星
       int i=1;
       while(i<=4){
           int j=1;
           while(j<=4-i){
               System.out.print(" ");
               j++;
           }
           int k=1;
           while(k<=2*i-1){
                System.out.print("*");
                k++;
           }
           i++;
           System.out.println();
       }
       */
       /*
       //求相遇时间？
       int m = 1000;
       int h = 0;
       while(m>0){
           m -= 18;
           m -= 7; 
           h++;         
        }
       System.out.print(h+"小时后相遇"); 
       */
       

       //求几天买完？
       int s = 1020;
       int d = 0;
       while(s>0){
           s= s/2-2;
           d++;
       }
       System.out.print(d+"天后买完");


    }        
}








