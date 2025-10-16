'''
Q2. Write a java program to take a user input
and print each even digits of the number
one by one.
Input:
N=43705;
Output:
0
4
'''

def printNumber(n):
    while n > 0:    
        digit = n % 10
        if digit % 2 == 0:
        # if digit % 2 != 0:     for odd digit
            print(digit)
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
        while (n > 0){
            int digit = n%10;
            if (digit % 2 == 0){
            System.out.println(digit);
            }
            n /= 10;
        }
        return n;
    }
}
'''


# javascript code 
'''
function printNumber(n){
    while (n > 0){
        let digit = n%10;
        if (digit %2== 0){
            console.log(digit);
        }
        n = Math.floor(n/10);
    }
}

n = Number(prompt('Enter a number: '));
printNumber(n);
'''