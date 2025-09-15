# Q4. WAJP to print sum of squares of all
# natural numbers from 1 to 100.

# 1^2 + 2^2 + 3^2 + 4^2 + ... upto 100

def square_sumNatural(n):
    square_sum = 0
    i = 1
    while i <= n:
        square_sum += i**2
        # square_sum += i**3   # to find cube
        i += 1
    return square_sum
n = int(input('Enter number to find sum of square of all natural number: '))
result = square_sumNatural(n)
print(f'Sum of Square of {n} is {result}')


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
let n = Number(prompt('Enter a number to find sum of squares of all natural number: '));
let result = sum_of_squares(n);
console.log("Sum of squares of fist " +n+ " natural numbers is: "+result);

function sum_of_squares(n){
    let sum = 0;
    let i = 1;
    while (i <= n){
        sum += i * i;
        i++;
    }
    return sum
}

'''

# Q5. WAJP to print sum of cubes of all natural
# numbers from 1 to 100.

# 1^3 + 2^3 + 3^3+ 4^3 + ...... upto 100