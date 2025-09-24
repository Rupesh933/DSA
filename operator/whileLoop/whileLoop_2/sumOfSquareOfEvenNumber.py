# Q6. WAJP to print sum of squares of all even
# numbers from 1 to 100.

# 2^2 + 4^2 + 6^2 + 8^2... upto 100

def sum_of_square_Even1(n):
    sum = 0
    i = 1
    while i <= n:
        if i % 2 == 0:    # time complexity
            sum += i ** 2
        i += 1
    return sum 

def sum_of_square_Even2(n):
    sum = 0
    i = 2
    while i <= n:
        sum = i**2
        i += 2
    return sum

n = int(input("Enter number: "))
result1 = sum_of_square_Even1(n)
print(f'Sum of squares of even natural numbers up to {n} is: {result1}')

result2 = sum_of_square_Even2(n)
print(f'Sum of squares of even natural numbers up to {n} is: {result1}')



# java code
'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to find sum of squares of all natural numbers: ");
        int n = sc.nextInt();
        int result = sum_of_squares(n);
        System.out.println("Sum of squares of first " + n + " natural numbers is: " + result);
    }
    public static int sum_of_squares(int n){
        int sqr_sum = 0;
        int i = 1;
        while (i <= n){
            sqr_sum += i*i;
            i++;
        }
        return sqr_sum;
    }
}

'''

# javascript code
'''
let n = Number(prompt("Enter a number: "));
let result = sum_of_square(n);
console.log(`Sum of square of first ${n} natural number is: ${result}`);

function sum_of_square(n){
    let sqr_sum = 0;
    let i = 1;
    while (i <= n){
        sqr_sum += i*i;
        i++;
    }
    return sqr_sum;
}

'''

