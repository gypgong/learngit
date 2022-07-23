/*
public class TaskLoopTwo{
    public static void main(String[] args){
        int count =4;
        for(int i=1;i <=count;i++){
            //左边 画空格+画数字
            for(int j=1;j<=count-i;j++){
                System.out.print(" ");
            }
            for(int j=1;j<=i;j++){
                System.out.print(j);
            }
            //右边首行画空格
            if(i==1){
                for(int j=1;j<=count;j++){
                    System.out.print(" ");
                }
            }else{
            //填数字
            for(int j=1;j<=i-1;j++){
                System.out.print(i-j);
            }
            //for(int j=1;j<=4-i;j++){
            //    System.out.print(" ");
            //}
            }
            System.out.println();
        }
    }
}*/

//方法二
public class TaskLoopTwo{
    public static void main(String[] args){
        int count=9;
        //画空格+画数字+画数字
        for(int i=1;i <=count;i++){
            //左边 画空格+画数字
            for(int j=1;j<=count-i;j++){
                System.out.print(" ");
            }
            for(int j=1;j<=i;j++){
                System.out.print(j);
            } 
            for(int j=i;j>1;j--){
                System.out.print(j-1);
            }
            System.out.println();               
        }        
    }
}