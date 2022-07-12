//求数组极值问题？
public class Array4{
    public static void main(String[] args){
        int[] a = {1,3,5,7,9,0,2,4,5,6,8};
        int min = a[0];//新建变量min,记录每次循环最小值
        int max = a[0];//新建变量max,记录每次循环最大值
        for(int i=0;i<a.length;i++){
            if(min>a[i]){
                min = a[i];
            }
            if(max<a[i]){
                max = a[i];
            }        
        }
        System.out.println("最大值"+max);
        System.out.println("最小值"+min);       
    }
}