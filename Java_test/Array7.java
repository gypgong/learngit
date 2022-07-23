public class Array7{
    public static void main(String[] args){

        //给定一个数组a{1,2,3,0,0,4,5,0,6,0,7} 去掉数组中的0元素（创建一个新的数组 短的 非零元素挑出来）

        int[] a = new int[]{89,0,1,0,2,3,0,0,4,5,0,6,0,7};//静态初始化数组a
        
        //找出原数组中为0的元素个数
        int x =0;
        for(int i=0;i<a.length;i++){
            if(a[i]==0){
                x++;
            }        
        }
        //动态初始化长度为a.length-x的新数组
        int[] newarray = new int[a.length-x];
        int index = 0;
        for(int i=0;i<a.length;i++){
            if(a[i]!= 0){//将旧数组中非0的元素存入到新数组中
              newarray[index] = a[i];
              index++;
            }             
        }
        //使用增强for循环输出新数组中元素，验证上面去零操作是否正确
        for(int v:newarray){
            System.out.println(v);
        }
    }
}