# Q3. WAJP to print sum of all Odd numbers
# from 1 to 100.
# 1+3+5+7+.........upto 100

def odd_sumNatural(n):
    odd_sum = 0
    i = 1
    while i <= n:
        odd_sum += i
        i += 2
    return odd_sum

n = int(input('Enter number to find sum of odd: '))
result = odd_sumNatural(n)
print(f'sum of odd number of {n} is: {result}')


# java code

'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number to find sum of odd number: ");
        int n = sc.nextInt();
        int result = odd_sumNatural(n);
        System.out.print("Sum of odd natural number of "+n+ " is: "+result);
    }
    public static int odd_sumNatural(int n){
        int odd_sum = 0;
        int i = 1;
        while (i <= n){
            odd_sum += i;
            i += 2;
        }
        return odd_sum;
    }
}

'''

# javascrip code

'''
let n = Number(prompt("Enter number to find sum of odd number: "));
let result = odd_sumNatural(n)
console.log("Sum of odd natural number of "+n+ " is: "+result)

function odd_sumNatural(n){
    let odd_sum = 0;
    let i = 1;
    while (i <= n){
        odd_sum += i;
        i += 2;
        }
    return odd_sum;
}

'''