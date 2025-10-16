# Q21. WAJP to accept a number from user and
# print sum of all its factors(number itself
# excluded).
# i/p: 14
# o/p: sum is: 10 (1+2+7)

def sum_of_its_factor(n):
    sum = 0
    i = 1
    while i < n:
        if n % i == 0:
            sum += i
        i += 1
    return sum
n = int(input('Enter a number: '))
print(sum_of_its_factor(n))


# java code
'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int result = sum_of_all_factorial(n);
        System.out.println("sum of all its factorial " + n + " is: " + result);
    }
    public static int sum_of_all_factorial(int n){
        int total = 0;
        int i = 1;
        while (i < n){
            if (n % i == 0){
            total += i;
            }
            i++;
        }
        return total;
    }
}
'''

# javascript code
'''
let n = Number(prompt("Enter a number: "));
let result = sum_of_square(n);
console.log(`sum of all its factor ${n} is: ${result}`);

function sum_of_its_factor(n){
    let total = 0;
    let i = 1;
    while (i <= n){
        if (n%i == 0){
        total += i;
        }
        i++;
    }
    return sqr_sum;
}
'''