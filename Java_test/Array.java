public class Array{
    public static void main(String[] args){
        //将1-100之间的偶数存到一个数组中

        //动态初始化一个长度为50的数组
        int[] array = new int[50];
        //int[0] = 2;
        //int[1] = 4;
        //int[2] = 6;
        //int[3] = 8;
        //int[4] = 10;

        //将1-100之间的偶数，存入到数组中
        for(int i=0;i<array.length;i++){
            array[i] = 2*i+2;
        }
        //验证下上面的存入是否正确；使用增强for循环输出一些数组中的元素
        for(int v:array){
            System.out.println(v);
        }
    }
}