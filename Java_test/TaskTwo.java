//方法一
public class TaskTwo{
    public static void main(String[] args){
        for(int x=1;x<50;x++){
            if((x*2)+4*(50-x) == 160){
                System.out.println(x);
                System.out.println(50-x);
            }
        }
    }
}



/*
方法二（会报错）
public class TaskTwo{
    public static void main(String[] args){
        int x =1;
        int y =1;
        for(;x<50 && y<50;x++ && y++){
            if(x+y==50 &&(x*2)+(y*4) == 160){
                System.out.println(x);
                System.out.println(y);
            }
        }
    }
}
*/
