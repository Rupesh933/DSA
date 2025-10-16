'''
Q5. Write a java program to take a user input
and print the biggest digit of the number.
Input:
N=43705;
Output:
7
'''
def printNumber(n):
    biggest = 0
    
    while n > 0:
        digit = n % 10  # last digit
        if digit > biggest:
            biggest = digit
        n //= 10
    print(f'Biggest number is: {biggest}')

printNumber(43705)


# java codes
'''
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        
        int result = printNumber(n);   // function call
        System.out.println("Biggest digit is: " + result);
    }

    public static int printNumber(int n) {
        int biggest = 0;
        while (n > 0) {
            int digit = n % 10;
            if (digit > biggest) {
                biggest = digit;
            }
            n /= 10;
        }
        return biggest;   // return biggest, not n
    }
}
'''

# javascript 
'''
let n = Number(prompt('Enter a number: '))
console.log(printNumber(n));

function printNumber(n){
    let biggest = 0;
    while n > 0{
        let digit = n % 10;
        if (digit > biggest){
            biggest = digit;
        }
        n /= 10;
    }
    return biggest;
}
'''