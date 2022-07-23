public class TaskOne{
    public static void main(String[] args){
        for(int x=1;x<370;x++){
            if((x-10)+(x+20)+(x/2)+(x*2) == 370){
                System.out.println(x-10);
                System.out.println(x+20);
                System.out.println(x/2);
                System.out.println(x*2);
            }        
        }      
    }
} 