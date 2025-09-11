# Q14. WAJP to check whether the three sides of
# a triangle is valid or not.
# a+b > c
# a+c > b 
# b+c > a

a = 2
b = 5
c = 0

check = f'Triangle is valid ' if a+b > c and a+c> b and b+c>a else 'Triangle is not valid'
print(check)

# java code

'''
import java.util.Scanner;
class Main {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();   // full line input
        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();
        System.out.print("Enter third number: ");
        int num3 = sc.nextInt();
        String check = ( num1 + num2 > num3 && num1 +num3 > num2 && num2 + num3 > num1 ) ? "Triangle is valid" : "Triangle is not valid";
        System.out.println(check);
        sc.close();
    }
}

'''

# javascript code

'''
let num1 = prompt("Enter first number: ")
let num2 = prompt("Enter second number: ")
let num3 = prompt("Enter third number: ")
let check = ( num1 + num2 > num3 && num1 +num3 > num2 && num2 + num3 > num1 ) ? "Triangle is valid" : "Triangle is not valid";
console.log(check)

'''