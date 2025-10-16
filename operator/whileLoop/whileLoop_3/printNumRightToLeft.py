'''
Q1. program to take a user input and print each
digits of the number one by one from right to left.
Input:
N=43705;
Output:
5
0
7
3
'''
def printNumber(n):
    while n > 0:  
        print(n%10)    
        n = n // 10      
printNumber(43705)




# java code 
'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        System.out.println("After no: ");
        int result = printNumber(n);
    
    }
    public static int printNumber(int n){
        int i = 0;
        while (n > 0){
            System.out.println(n%10);
            n /= 10;
            i++;
        }
        return n;
    }
}
'''

# javascript code 
'''
function printNumber(n){
    let i = 0;
    while (n > 0){
        console.log(n%10);
        n = Math.floor(n/10);
        i++;
    }
}

n = Number(prompt('Enter a number: '));
printNumber(n);
'''