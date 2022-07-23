public class Test {
	public static void main(final String[] args) {
		final int count = 4;
		for(int i=1;i<=count;i++){
			//首行画星星
			if(i==1){
				for(int j=1;j<= 7;j++){
                    System.out.print("* ");
                }
			}else{
				//画星星
				for(int j=1;j<=count+1-i;j++){
					System.out.print("* ");
				}
				//画空格
				for(int j=1;j<=2*i-3;j++){
					System.out.print("  ");
				}
				//画星星
				for(int j=1;j<=count+1-i;j++){
					System.out.print("* ");
				}
			}
			System.out.println();
		}
		}
}