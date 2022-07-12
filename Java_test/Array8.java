//创建一个数组 存储2-100直接的素数（质数）
public class Array8{
    public static void main(String[] args){

        /*
        //方法一(推荐使用，循环执行次数少一些，性能上会好很多)
        int[] array = new int[50];//1.动态初始化一个足够长的数组array
        //2.找出2-100之间的质数，并存依次入到array数组中
        int index = 0;
        for(int num=2;num<=100;num++){
            boolean x = false;
            for(int i=2;i<num-1;i++){
                if(num%i==0){
                    x = true;
                    break;
                }            
            }
            if(x==false){
                array[index] = num;
                index++;                 
            }                
        }
        //3.去除array数组中的零元素
        int[] newarray =new int[index];
        for(int i=0;i<array.length;i++){
            if(array[i]!=0){
                newarray[i] =array[i];
            }
        }
        array = null;//4.清空原数组

        for(int v:newarray){//5.输出新数组中元素检查
            System.out.println(v);        
        }

        */

        //方法二（不推荐使用，多次使用嵌套循环，性能影响比较大）
        //1.找出找出2-100之间的质数（素数）个数 count
        int count = 0;
        for(int num=2;num<=100;num++){
            boolean x = false;
            for(int i=2;i<num;i++){
                if(num%i==0){
                    //System.out.println(num+"不是素数");
                    x = true;
                    break;
                }
            }
            if(!x){
                //System.out.println(num+"是素数");
                count++;
            }
        }            
        int[] array = new int[count];//2.动态初始化长度为count的数组array
        int index =0;
        
        for(int num=2;num<=100;num++){
            boolean x = false;
            for(int i=2;i<num;i++){
                if(num%i==0){
                    //System.out.println(num+"不是素数");
                    x = true;
                    break;
                }
            }
            if(!x){
                //System.out.println(num+"是素数");
                array[index] = num;
                index++;
            }
        }
        for(int v:array){
            System.out.println(v);
        }   

    }
}