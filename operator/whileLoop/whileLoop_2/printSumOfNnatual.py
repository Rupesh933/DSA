# Q1. print sum of n natural number from 1 to 100
# 1 + 2 + 3 + ...... + 100
def sum_natural(n):
    sum = n * (n + 1)
    return sum / 2    # 100×(100+1)=100×101=10100  =>  10100 // 2 = 5050

n = int(input('Enter number: '))
result = sum_natural(n)
print(f'sum of {n}th natural number is: {result}')


# java code
'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = sc.nextInt();
        int result = sum_natural(n);
        System.out.print("Sum of "+n+"th natural number is: "+result);
    }
    public static int sum_natural(int n){
        int sum = (n * (n + 1)) / 2;
        return sum;
    }
}

'''

# javascrip code

'''
let n = Number(prompt('Enter number: '));   // input converted to number
let result = sum_natural(n);
console.log("Sum of "+n+"th natural number is: "+result);

function sum_natural(let n){
    let sum = (n*(n+1))/2;
    return sum;
}

'''