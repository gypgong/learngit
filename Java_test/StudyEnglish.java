import java.util.Scanner;

public class StudyEnglish{
    public static void main(final String[] args) {
        final Scanner input = new Scanner(System.in);
        System.out.println("Please enter a number:");
        final int day = input.nextInt(); // input.nextLine()；读取文字
        //final int day = 1;
        if(day==1){
            System.out.println("星期一Monday");
        }else if(day==2){
            System.out.println("星期二Tuesday");
        }else if(day==3){
            System.out.println("星期三Wednesday");
        }else if(day==4){
            System.out.println("星期四Thursday");
        }else if(day==5){
            System.out.println("星期五Friday");
        }else if(day==6){
            System.out.println("星期六Saturday");
        }else if(day==7){
            System.out.println("星期天Sunday");
        }else{
            System.out.println("错误输入error");
        }
    }
}