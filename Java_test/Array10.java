//使用数组模拟登录操作问题 
import java.util.Scanner;
//Scanner input = new Scanner(System.in);
//System.out.println("请输入一个学生分数");
//int month = input.nextInt();//帮我们读取输入的数字， input.nextLine()；读取输入的文字

public class Array10{
    public static void main(final String[] args) {
        final String[] usernamebox = new String[] { "张三", "李四", "王五", "赵六" };// 静态初始化帐号数组
        final int[] passwordbox = new int[] { 123, 666, 888, 000 };// 静态初始化密码数组

        final Scanner input = new Scanner(System.in);// 动态初始化一个Scanner型的数组

        System.out.println("请输入帐号");
        final String username = input.nextLine(); // input.nextInt();读取输入的数字， input.nextLine()；读取输入的文字

        System.out.println("请输入密码");
        final int password = input.nextInt(); // input.nextInt();读取输入的数字， input.nextLine()；读取输入的文字

        boolean x = false;
        //最初方案 （提示语存在安全隐患）
        /*  
        for(int i=0;i<usernamebox.length;i++){
            if(usernamebox[i].equals(username)){//判断帐号是否正确
                if(passwordbox[i]==password){//判断密码是否正确
                    System.out.println("登录成功Successful login");
                }else{
                    System.out.println("密码不对The password is wrong");
                }
                x = true;
                break;
            }                         
        }
        if(x == false){
            System.out.println("帐号不存在Account does not exist");
        } 
        */
        
        System.out.println("==================");        
        
        //优化下，只提示“帐号或密码不对”  个人理解：1、登录则成功更改标记，未登录成功则标记不改变；2、标记只有未更改则认为未登录成功，提示“密码或帐号不对”
        for(int i=0;i<usernamebox.length;i++){
            if(usernamebox[i].equals(username)){//判断帐号是否正确
                if(passwordbox[i]==password){//判断密码是否正确
                    System.out.println("登录成功Successful login");
                    x = true;
                }
                break;
            }                         
        }
        if(x == false){
            System.out.println("帐号或密码不对Incorrect account or password");
        } 
    }
}