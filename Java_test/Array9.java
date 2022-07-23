//数组冒泡排序问题
public class Array9{
    public static void main(String[] args){
        int[] a =new int[]{9,8,7,6,5,3,1,1,2,5,8,7,4};
        for(int j=1; j<a.length;j++){//循环比较一轮（几个元素则比较length轮），每次冒出一个最小值
            for(int i=a.length-1;i>=j;i--){//从数组尾元素 一直比较到首元素，需比较length-1次
                if(a[i]<a[i-1]){//比较当前元素比前一个元素小，则交换两个元素位置
                    a[i] = a[i]^a[i-1];
                    a[i-1] = a[i]^a[i-1];
                    a[i] = a[i]^a[i-1];
                }
            } 
        }        
        for(int v:a){
            System.out.println(v);
        }
    }
}