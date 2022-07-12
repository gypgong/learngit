import java.util.Scanner;
public class TaskLoopOne {
	public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        System.out.println("请输入数字");
		int count= input.nextInt(); //input.nextLine()；读取字符  input.nextInt()读取数字
		for(int i=1;i<=count;i++){
			//首行画星星
			if(i==1){
				for(int j=1;j<= count*2-1;j++){
                    System.out.print("* ");
                }
			}else{
				//画星星
				for(int j=1;j<=count+1-i;j++){
					System.out.print("* ");
				}
				//画空格
				for(int j=1;j<=2*i-3;j++){
					System.out.print("  ");
				}
				//画星星
				for(int j=1;j<=count+1-i;j++){
					System.out.print("* ");
				}
			}
			System.out.println();
		}
		}
}