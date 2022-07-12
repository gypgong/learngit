public class Array1{
    public static void main(String[] args){
        //
        int[] arraya = {1,2,3,4};
        int[] arrayb = {5,6,7,8};

        //换数组引用，直接在站内存交换数组引用 (推荐使用)
        int[] temp =arraya;//借用一个中间数组，临时装一下arraya数组
        arraya = arrayb;
        arrayb = temp;
                
        /*
        //换数组中的值
        for(int i=0;i<arraya.length;i++){
            //No1、借助中间量交换 
            //int temp = arraya[i];
            //arraya[i] = arrayb[i];
            //arrayb[i] = temp; 

            //No2、位运算
            /*
            int x = 10; 
            int y = 20; 
            x = x ^ y; 
            y = x ^ y; 
            x = x ^ y;
            此种方法运用这种原理：一个数对另一个数位异或两次，该数不变
            x = x ^ y;  此时x的值为x ^ y;
            y = x ^ y;  此时的x经上面的运算变成x ^ y，所以y =  x ^ y ^ y = x;
            x = x ^ y;  此时的y经上面的运算变成 x，所以x =  x ^ y ^ x = y; 实现两个数的互换  */
            
            /*
            arraya[i] = arraya[i]^arrayb[i];
            arrayb[i] = arraya[i]^arrayb[i];
            arraya[i] = arraya[i]^arrayb[i];
            
            //No3、数值相加减交换
            arraya[i] = arraya[i]+arrayb[i];
            arrayb[i] = arraya[i]-arrayb[i];
            arraya[i] = arraya[i]-arrayb[i];            
        }
        */

        for(int v:arraya){
            System.out.println(v);
        }
        System.out.println("==================");
        for(int v:arrayb){
            System.out.println(v);
        }
    }
}