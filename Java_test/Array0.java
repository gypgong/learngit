public class Array0{
    public static void main(String[] args){
        //将1-100之间的奇数存到一个数组中

        //动态初始化一个长度为50的数组
        int[] array = new int[50];
        //int[0] = 1;
        //int[1] = 3;
        //int[2] = 5;
        //int[3] = 7;
        //int[4] = 9;

        //将1-100之间的奇数存到array数组中
        for(int i=1;i<array.length;i++){
            array[i] = 2*i+1;
        }

        //验证下上面的存入是否正确；使用增强for循环输出一下数组中元素
        for(int v:array){
            System.out.println(v);
        }
    }
}