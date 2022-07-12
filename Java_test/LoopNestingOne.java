public class LoopNestingOne{
    public static void main(String[] args){
        /*画星星*/
        //System.out.print("*");
        /*换行*/
        //System.out.println();
        //i 行数；j每行星星数
        /*int count =4;
        for(int i=1;i <= count;i++){
            for(int j=1;j<=4-i;j++){
                System.out.print("#");
            }            
            for(int j=1;j<=i;j++){
                System.out.print(" * ");
            }
            System.out.println();
        }
        //System.out.println();
        */

        int count =9;
        for(int i=1;i <= count;i++){
            //画空格+画数字
            for(int j=1;j<=count-i;j++){
                System.out.print(" ");
            }
            for(int j=1;j<=i;j++){
                System.out.print(j);
            }
            //画#
            if(i==1){
                for(int j=1;j<=count;j++){
                    System.out.print(" ");
                }
            }else{
                //画*+画#
            for(int j=1;j<=i-1;j++){
                System.out.print(i-j);
            }
            for(int j=1;j<=4-i;j++){
                System.out.print(" ");
            }
            }
            System.out.println();
        }


    }
}
