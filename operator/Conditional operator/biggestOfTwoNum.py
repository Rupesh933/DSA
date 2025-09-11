# Q19. WAJP to print the bigger of two numbers.
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
check = f'{first} is bigger' if first > second else f'{first} and {second} both are same' if first == second else f'{second} is bigger'
print(check)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
check = f'{a} is bigger' if a > b and a > c else f'{b} is bigger' if b > a and b > c else f'{a} {b} {c} are same' if a == b == c else f'{c} is bigger'
print(check)

# java code 

'''
import java.util.Scanner;
class Main{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a first number: ");
        int a = sc.nextInt();
        System.out.print("Enter a second number: ");
        int b = sc.nextInt();
        String check = (a > b) ? a+ " is bigger" : (a == b) ? a+ " and " +b+ " both are same" : b+ " is bigger";
        System.out.print(check);
    }
}

'''

# javascript code

'''
let a = prompt("Enter first Number: ") 
let b = prompt("Enter second Number: ")
let check = (a > b) ? a+ " is bigger" : (a == b) ? a+ " and " +b+ " both are same" : b+ " is bigger";
console.log(check);

'''


# Q20. WAJP to print the smaller of two
# numbers.

# Q21. WAJP to print the biggest of three
# numbers.

# Q22. WAJP to print the smallest of three
# numbers.

# Q23. WAJP to print the biggest of four
# numbers.

# Q24. WAJP to print the smallest of four
# numbers.