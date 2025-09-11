# Q13. For given numbers x and y. check whether
# y is a factor of x or not.
# Input: x=12, y=4
# Output: x is a factor of y

x = 12
y = 6
check = f" {x} % {y} = 0 x is factor of y" if x % y == 0 else f'{x} % {y} = {x%y} x is not factor of y '
print(check)


# java code 

'''

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();

        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();

        String check = (num1 % num2 == 0) 
            ? (num1 + " % " + num2 + " = 0 → " + num1 + " is factor of " + num2) 
            : (num1 + " % " + num2 + " = " + (num1 % num2) + " → " + num1 + " is not factor of " + num2);

        System.out.println(check);
    }
}

'''


# javascript code 

'''
let num1 = prompt("Enter first number: ");
let num2 = prompt("Enter second number: ");

let check = (num1 % num2 == 0) 
            ? (num1 + " % " + num2 + " = 0 → " + num1 + " is factor of " + num2) 
            : (num1 + " % " + num2 + " = " + (num1 % num2) + " → " + num1 + " is not factor of " + num2);
console.log(check);

'''


