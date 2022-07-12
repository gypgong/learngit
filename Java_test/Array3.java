public class Array3{
    public static void main(String[] args){
        int[] a = {1,2,3,4,5,6,9,8,5}; 
        int x = 0;      
        for(int i=0;i<a.length;i++){//先对数组求和x
             x += a[i];           
        }
        System.out.println(x/a.length);//输出数组平均值
    }
}
