public class Array2{
   public static void main(String[] args){
        //一个数组中元素头尾互换
       int[] a = {1,2,3,4,5,6,7};
       for(int i=0;i<a.length/2;i++){
            //int x = a[i];
            //a[i] = a[(a.length-1)-i];
            //a[(a.length-1)-i] = x;
        
            //使用位运算交换元素位置
            a[i] = a[i]^a[(a.length-1)-i];
            a[(a.length-1)-i] = a[i]^a[(a.length-1)-i];
            a[i] = a[i]^a[(a.length-1)-i];
       }
       for(int v:a){//输出数组中元素，验证数组中元素交换是否正确
            System.out.print(v);            
       }
   } 
}
