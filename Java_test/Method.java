public class Method {
    
//0、画星星--倒三角形 不确定方向和行数
    public void Drawstar(int line,boolean f){
        for(int i=1;i<=line;i++){
            if(f==false){
                for(int j=1;j<=i-1;j++){
                    System.out.print(" ");
                }
            }
            for(int j=1;j<=line+1-i;j++){
                System.out.print("*");
            }                        
            System.out.println();
        }        
    }


    //1、交换两个数组元素
    public int[][] exchange(int[] a,int[] b){
        
        //借用临时数组-交换数组引用
        
        int[] temp = a;
        a = b;
        b =temp;
        int[][] result = {a,b};
        return result;      
    }

    //2、交换一个数组的头尾元素位置
    public void exchange1(int[] x){
        //打印原数组（仅学习使用）
        System.out.print("原数组为：");
        for(int v:x){
            System.out.print(v+"\t");           
        }
        System.out.println();

        //将数组中元素首尾互换位置
        for(int i=0;i<x.length/2;i++){
            //int temp = x[i];
            //x[i] = x[(a.length-1)-i];
            //x[(x.length-1)-i] = temp;
        
            //使用位运算交换元素位置
            x[i] = x[i]^x[(x.length-1)-i];
            x[(x.length-1)-i] = x[i]^x[(x.length-1)-i];
            x[i] = x[i]^x[(x.length-1)-i];

        }
        //打印新数组（仅学习使用）
        System.out.println("-------------");
        System.out.print("新数组为：");
        for(int v:x){
            System.out.print(v+"\t");                       
        }
        System.out.println();
    }    


    //3、找寻数组中的极值（int-最大值max、最小值min）
    public int[]  exchange2(int[] array){
        int max = array[0];
        int min = array[0];
        for(int i=0;i<array.length;i++){
            if(max < array[i]){
                max = array[i];
            }
            if(min > array[i]){
                min = array[i];
            }
        }        
        int[] x ={max,min};
        return x;

    }

    //4、找寻给定元素是否在数组内存在

    public boolean exchange3(int e, int[] array2) {
        boolean zz = false;
        for(int v:array2){
            if(v==e){
                zz = true;
                break;                              
            }                       
        }
        return zz;
    }

    //5、用来合并两个数组
    public int[] exchange4(int[] arrayaa,int[] arraybb){
        int[] newarray = new int[arrayaa.length+arraybb.length];
        for(int i=0;i<arrayaa.length;i++){
            newarray[i] = arrayaa[i];
        }
        for(int i=0;i<arraybb.length;i++){
            newarray[arrayaa.length+i] = arraybb[i];
        }
        
        return newarray;
    }

    //6、用来将一个数组按照最大值位置拆分
    public int[][] exchange5(int[] oldarray){
        int max = oldarray[0];
        int index = 0;
        for(int i=0;i<oldarray.length;i++){
            if(max < oldarray[i]){
                max = oldarray[i];
                index = i;
            }
        }
        int[] newarraya = new int[index];//不取最大值（剔除最大值）
        int[] newarrayb = new int[oldarray.length-index-1];
        for(int i=0;i<newarraya.length;i++){
            newarraya[i] = oldarray[i];
        }
        for(int i=0;i<newarrayb.length;i++){
            newarrayb[i] = oldarray[index+i+1];
        }
        int[][] newarray1 = {newarraya,newarrayb};
        return newarray1;
    }

    //7、用来去掉数组中的0元素
    public int[] exchange6(int[] oldarray1){
        int[] temparray = new int[oldarray1.length];
        int index = 0;
        for(int i=0;i<oldarray1.length;i++){
            if(oldarray1[i]!= 0){
                temparray[index++] = oldarray1[i];                
            }
        }
        System.out.println("旧数组中非0元素个数："+index);
        int[] newarray2 = new int[index];
        for(int i=0;i<newarray2.length;i++){
            newarray2[i] = temparray[i];
        }
        temparray = null;
        return newarray2;
    }

    
    //10、用来实现模拟用户登录认证（二维数组当做小数据库）
    public boolean exchange7(String username,String password,String[][] data){
        boolean stamp = false;
        for (String[] element : data) {
            if (element[0].equals(username)) {// 判断帐号是否正确
                if (element[1].equals(password)) {// 判断密码是否正确
                    stamp = true;
                    // System.out.println("帐号+密码正确，登录成功");
                }
            }
            System.out.println("此时的stamp的值为：" + stamp);
            break;
        }
        return stamp;
        
    }

}
    