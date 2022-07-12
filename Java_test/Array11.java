//使用多维数组模拟登录操作问题 
import java.util.Scanner;
public class Array11{
    public static void main(final String[] args) {
        final String[][] account = new String[][] { { "张三", "123" }, { "李四", "000" }, { "王五", "666" },
                { "赵六", "888" } };

        final Scanner input = new Scanner(System.in);

        System.out.print("请输入帐号:");
        final String username = input.nextLine();

        System.out.print("请输入密码:");
        final String password = input.nextLine();

        System.out.println("==============");

        boolean x = false;
        for(int i=0;i<account.length;i++){
            if(account[i][0].equals(username)){
                if(account[i][1].equals(password)){
                    x = true;
                    System.out.println("登录成功Login successfully");                    
                }
            }
            break;
        }
        if(x==false){
            System.out.println("帐号或密码不对Incorrect account or password");
        }
    }
}