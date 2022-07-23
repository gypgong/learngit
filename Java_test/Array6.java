//给定一个数组，按照数组中最大值位置，将数组拆分未两个数组

public class Array6{
    public static void main(String[] args){
        int[] a = {1,2,3,9,4,5};
        int max =a[0];
        int index = 0;
        for(int i=0;i<a.length;i++){
            if(max<a[i]){//使用循环方式找出原数组中最大的元素
                max = a[i];
                index++;//输入原数组中最大元素的位置
            }
        }
        //创建两个新的数组
        int[] new1 = new int[index];
        int[] new2 = new int[a.length-1-index];

        //从旧数组中取出元素分别存入到新数组中
        for(int i=0;i<new1.length;i++){
            new1[i] = a[i];
        }
        for(int i=0;i<new2.length;i++){
            new2[i] = a[index+1+i];
        }

        //使用增强for循环分别输出两个新数组中的元素，验证上面拆分过程是否正确
        for(int v:new1){
            System.out.println(v);
        }
        System.out.println("===========");//华丽的分割符
        for(int v:new2){
            System.out.println(v);
        }
    }
}