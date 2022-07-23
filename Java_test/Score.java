import java.util.Scanner;
public class Score{
    public static void main( String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请输入分数：");
        int marks = input.nextInt();
        if(marks < 60){
            System.out.println("不及格Fail");
        }else if(60 <= marks && marks < 70){
            System.out.println("Pass");
        }else if(70 <= marks && marks < 80){
            System.out.println("Middle ");
        }else if(80 <= marks && marks < 90){
            System.out.println("良好Good");
        }else if(90 <= marks && marks < 100){
            System.out.println("优秀Excellent");
        }else if(marks == 100){
            System.out.println("满分Full Marks");
        }else{
            System.out.println("Error");
        }
    }
}