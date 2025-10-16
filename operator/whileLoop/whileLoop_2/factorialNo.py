'''
Q19. WAJP to accept a input from user and
print factorial of that number.
i/p: 6!
o/p: 720
'''
def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i 
        i+=1
    return fact

n = int(input("Enter a number: "))
print(factorial(n))


# java code
'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to find factorial of numbers: ");
        int n = sc.nextInt();
        int result = factorial(n);
        System.out.println("Factorial of " + n + " is: " + result);
    }
    public static int factorial(int n){
        int fact = 1;
        int i = 1;
        while (i <= n){
            fact *= i;
            i++;
        }
        return fact;
    }
}
'''
# javascript code
'''
let n = Number(prompt("Enter a number: "));
let result = factorial(n);
console.log(`Factorial of ${n} is: ${result}`);

function factorial(n){
    let fact = 0;
    let i = 1;
    while (i <= n){
        fact *= i;
        i++;
    }
    return fact;
}

'''