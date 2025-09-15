# Q2. WAJP to print sum of all even numbers
# from 1 to 100.
# 2+4+6+8+.........upto 100


def sum_evenNatural(n):
    even_sum = 0
    i = 2    # Pehla even number 2 hota hai
    while i <= n:   # Jab tak i, n se chhota ya barabar hai
        even_sum += i
        i += 2      # Next even number lene ke liye i me 2 add karte hai
    return even_sum

n = int(input('Enter number to find sum of even natural number: '))
result = sum_evenNatural(n)
print(f'Sum of even natural number {n} is {result}')


# java code

'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number to find sum of even number: ")
        int n = sc.nextInt();
        int result = sum_evenNatural(n);
        System.out.print("Sum of even natural number " +n+ " is: " +result);
    }
    public static int sum_evenNatural(int n){
        int even_sum = 0;
        int i = 2;   // first even number is 2
        while (i <= n){
            even_sum += i; 
            i += 2;
        }
        return even_sum;
    }
}

'''

# javascript code

'''
let n = Number(prompt('Enter number to find sum of even number: '));
let result = sum_evenNatural(n);
console.log("Sum of even natural number " +n+ " is: " +result);

function sum_evenNatural(n){
    let even_sum = 0;
    let i = 2;
    while (i <= n){
        even_sum += i;
        i += 2;
    }
    return even_sum;
}

'''