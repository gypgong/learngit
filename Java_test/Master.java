import java.util.Scanner;
public class Master {     
    public static void main(String[] args) {
       
        Person p = new Person();
        p.name = "张三";
        p.age = 18;
        p.sex = "男";

        Person p1 = new Person();
        p1.name = "李四";
        p1.age = 16;
        p1.sex = "女";

        System.out.println(p.name + "今年" + p.age + "岁，性别是" + p.sex);
        System.out.println(p1.name + "今年" + p1.age + "岁，性别是" + p1.sex);

        System.out.println("0、画倒三角 且可控制方向（false右、true左）===================================");

        // 初始化一个Method类型 m
        Method m = new Method();

        // 0、画倒三角 且可控制方向（false右、true左）
        m.Drawstar(9, true);

        System.out.println("1、交换两个数组位置===================================");
        // 1、交换两个数组位置

        int[] x = { 1, 2, 3, 4, 6, 55, 88 };
        int[] y = { 5, 6, 7, 8, 9 };
        int[][] value =m.exchange(x, y);
        x = value[0];
        y = value[1];
        for(int v:x){
            System.out.print(v+"\t");
        }
        for(int v:y){
            System.out.print(v+"\t");
        }

        System.out.println("2、交换一个数组的头尾元素位置===================================");
        // 2、交换一个数组的头尾元素位置
        int[] x = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        m.exchange1(x);

        System.out.println("3、找寻数组中的极值（int[]-最大值max,最小值min）===================================");
        // 3、找寻数组中的极值（int[]-最大值max,最小值min）
        // Method m = new Method();
        int[] array = { 8, 5, 69, 4, 1, 3, 69, 7, 4, 0, -5 };
        int[] array1 = m.exchange2(array);
        for (int v : array1) {
            System.out.println(v);
        }

        System.out.println("4、找寻给定元素是否在数组内存在 输入一个元素 返回true则表示存在===================================");
        //4、找寻给定元素是否在数组内存在 输入一个元素 返回true则表示存在
        Scanner input = new Scanner(System.in);
        System.out.println("请输入一个元素:");
        int e = input.nextInt();
        
        int[] array2 = {0,89,2,74,4,1,5,4,64,9,8,6,4,9};
        boolean F = m.exchange3(e, array2);
        System.out.println(F);


        System.out.println("5、用来合并两个数组===================================");
        //5、用来合并两个数组
        //Method m = new Method();
        int[] arrayaa = {1,2,3};
        int[] arraybb = {0,7,8,9,4,5,6};
        //m.exchange4(arraya, arrayb)--返回一个新的数组newarray
        for(int v:m.exchange4(arrayaa, arraybb)){
            System.out.print(v+"\t");
        }
        System.out.println();//换行


        System.out.println("6、用来将一个数组按照最大值位置拆分===================================");
        //6、用来将一个数组按照最大值位置拆分
        //Method m = new Method();创建一个Mehtod类的对象m
        int[] oldarray = {0,6,2,5,1,4,5,8,9,7};
        //m.exchange5(oldarray) 返回的是一个二维数组
        for(int[] arr:m.exchange5(oldarray)){
            for(int v:arr){
                System.out.print(v+"\t");
            }
            System.out.println();
        }


        System.out.println("7、用来去掉数组中的0元素===================================");
        //7、用来去掉数组中的0元素
        //Method m = new Method(); 创建一个Method类的对象m
        int[] oldarray1 = {11,0,2,5,8,7,0,7,9,0,2,0,0,00};
        int[] newarrayx = m.exchange6(oldarray1);//返回的是一个新数组
        for(int v:newarrayx){
            System.out.print(v+"\t");
        }
        System.out.println();

        //10、用来实现模拟用户登录认证（二维数组当做小数据库）
        Method m = new Method(); //创建一个Method类的对象m
        Sca
        nner input = new Scanner(System.in);
        System.out.println("请输入帐号：");
        String username = input.nextLine();
        
        System.out.println("请输入密码：");
        String password = input.nextLine();

        String[][] data ={{"张三","123"},{"李四","000"},{"王五","666"},{"赵六","888"}};
        
        //m.exchange7(username, password,data);
        if(m.exchange7(username, password,data)==false){
            System.out.println("登录不成功，密码或帐号错误");
        }else{
            System.out.println("登录成功");
        }

    }    
}