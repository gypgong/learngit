import java.util.Scanner;//导入Scanner相关包

public class SeasonDemo{
	public static void main(final String[] args) {
		/* 1.创建一个month变量 用来存储一个月份值（Scanner） */
		final Scanner input = new Scanner(System.in);
		System.out.println("请输入一个月份");
		final int month = input.nextInt();/* 帮我们读取输入的数字， input.nextine()；读取字 */
		/*2.通过month存储的值 进行季节的判断*/
		if(month==3||month==4||month==5){
			System.out.println("春天Spring");
		}else if(month==6||month==7||month==8){
			System.out.println("夏天Summer");
		}else if(month==9||month==10||month==11){
			System.out.println("秋天Autumn");
		}else if(month==12||month==1||month==2){
			System.out.println("冬天Winter");
		}else{
			System.out.println("错误Error");
		}        
	}
}