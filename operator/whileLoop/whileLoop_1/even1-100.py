# Q3. WAJP to print all the even numbers from 1 to 100.

i = 1 
while (i <= 100):
    if i % 2 == 0:
        print(i)
    i += 1

# java code 

'''
import java.util.Scanner;
class Main{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a year: ");
        int i = 1;
        while (i <= 100){
            if (i % 2 == 0) {
                System.out.println(i);
            }
            i ++;
        }
    }
}

'''

# javascript code

'''
let i = 1;
while (i <= 100){
    if (i % 2 == 0)
      {
        console.log(i);
    }
   i ++;
}

'''