public class Array5{
    public static void main(String[] args){
        int[] a = {1,2,3,90};
        int[] b = {4,5,888};

        //动态初始化一个数组
        int[] newarray = new int[a.length+b.length];

        //将a数组中的元素取出，依次放入到新的数组中
        for(int i=0;i<a.length;i++){
            newarray[i] = a[i];
        }
        //将b数组中的元素取出，依次放入到新的数组剩下的位置中
        for(int i=0;i<b.length;i++){
            newarray[a.length+i] = b[i];
        }

        //使用增强for循环输出新数组的元素，检查上面合并a和b的元素操作是否成功
        for(int v:newarray){
            System.out.println(v);
        }        
    }  
}