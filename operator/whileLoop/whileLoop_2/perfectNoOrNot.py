'''
Q22. WAJP to accept a number from user and
print the number is a perfect number or
not.
i/p: 28
o/p: 28 is a perfect number
Perfect number: if the sum of all factors of a
Number is equals to number itself then
It is a perfect number.
'''

def is_perfect(n):
    sum = 0
    i = 1
    while i < n:
        if n % i == 0:
            sum += i
        i += 1
    return sum == n 

n = int(input('Enter a number: '))
if is_perfect(n):
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')


# java code
'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to check number is perfect or not: ");
        int n = sc.nextInt();
        if (is_perfect(n)){
            System.out.println(n+ " is perfect number.");
        }
        else {
            System.out.println(n+ " is not perfect number");
        }
    }
    public static boolean is_perfect(int n){
        int total = 0;
        int i = 1;
        while (i < n){
            if (n % i == 0){
            total += i;
            }
            i++;
        }
        return total == n;
    }
}
'''

# javascript code 
'''
let n = Number(prompt("Enter a number to check number is perfect or not: "));
if (is_perfect(n)){
    console.log(n+ " is a perfect number.")
}
else{
    console.log(n+ " is not a perfect number.")
}

function is_perfect(n){
    let total = 0;
    let i = 1;
    while (i < n){
       if (n % i == 0){
          total += i;
       }
       i++;
    }
    return total == n;
}
'''