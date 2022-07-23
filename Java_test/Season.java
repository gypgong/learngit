/*
import java.util.Scanner;
public class Season{
    public static void main(String[] args){
        //int month = 30;
        Scanner input = new Scanner(System.in);
        int month =input.nextlnt();
        if(month==3){
            System.out.println("Spring");
        }else if(month==4){
            System.out.println("Spring");
        }else if(month==5){
            System.out.println("Spring");
        }else if(month==6){
            System.out.println("Summer");
        }else if(month==7){
            System.out.println("Summer");
        }else if(month==8){
            System.out.println("Summer");
        }else if(month==9){
            System.out.println("Autumn");
        }else if(month==10){
            System.out.println("Autumn");
        }else if(month==11){
            System.out.println("Autumn");
        }else if(month==12){
            System.out.println("Winter");
        }else if(month==1){
            System.out.println("Winter");
        }else if(month==2){
            System.out.println("Winter");
        }else{
            System.out.println("Error");
        }        
    }
}
*/

/*
import java.util.Scanner;
public class Season{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("请输入一个月份");
        int month =input.nextlnt();
        if(month==3||month==4||month==5){
            System.out.println("Spring");
        }else if(month==6||month==7||month==8){
            System.out.println("Summer");
        }else if(month==9||month==10||month==11){
            System.out.println("Autumn");
        }else if(month==12||month==1||month==2){
            System.out.println("Winter");
        }else{
            System.out.println("Error");
        }        
    }
}
*/
import java.util.Scanner;
public class Season{
	public static void main(final String[] args) {
        // 1.创建一个month变量 用来存储一个月份值（Scanner）
        final Scanner input = new Scanner(System.in);
        System.out.println("请输入一个月份");
        final int month = input.nextInt();// 帮我们读取输入的数字， input.nextine()；读取字
		//2.通过month存储的值 进行季节的判断
		if(month > 1||month < 12){
			System.out.println("Error");
		}else if(month >=3 && month <= 5){
			System.out.println("Spring");
		}else if(month >=6 && month <= 8){
			System.out.println("Summer");
		}else if(month >=9 && month <= 11){
			System.out.println("Autumn");
		}else{
			System.out.println("Winter");
		}        
	}
}
