import java.util.Scanner;
public class SwitchDemo{
    public static void main(String[] args){
        //1、创建一个input变量，使用Scanner输入学生分数
        Scanner input = new Scanner(System.in);
        System.out.println("请输入一个学生分数");
        int month = input.nextInt();//帮我们读取输入的数字， input.nextLine()；读取字
		//2.通过month存储的值 进行分数的判断
        switch(month/10){
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:   
        case 5:
                System.out.println("不及格");
                break;
        case 6:
                System.out.println("及格");
                break;
        case 7:
                System.out.println("中");
                break;
        case 8:
                System.out.println("良好");
                break;
        case 9:
                System.out.println("优秀");
                break;
        case 10:
                if(month==100){
                    System.out.println("满分");
                    break;                    
                }                
        default :
                System.out.println("错误");       
        }
    }
}