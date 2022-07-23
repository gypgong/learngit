import java.util.Scanner;
public class DemoOne{
    public static void main(final String[] args){
        //1、使用Scanner创建一个变量，用例存储输入的星期数
        final Scanner input = new Scanner(System.in);
        final int day = input.nextInt();//帮我们读取输入的数字， input.nextine()；读取字
        System.out.println("请输入一个星期数");
        //2、通过day存储的值，进行学习安排
        switch(day){
            case 1:
            case 3:
            case 5:
                System.out.println("学编程");
                break;
            case 2:
            case 4:
            case 6:
                System.out.println("学英文");
                break;
            case 7:
                System.out.println("用英文编程");
            default:
                System.out.println("错误");
        }
    }
}