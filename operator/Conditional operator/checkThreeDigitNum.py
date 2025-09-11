# Q11. write a program to check the given +ve number is three digit number or not
num = int(input("Enter a number: "))
result = f'Yes, Number({num}) is three digit' if num >= 100 and num <= 999 else f'No, Number({num}) is not three digit'
print(result)


# java code

'''
import java.util.Scanner;
class Main {
    public static void main(String[] args)
    {
       Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();   // full line input
        String result = ( num >= 100 && num <= 999 ) ? "Yes, Number("+num+") is three digit" : "No, Number("+num+") is not three digit";
        System.out.println(result);
    }
}

'''

# javascript code

'''
let num = prompt("Enter a number to check no. is three digit or not: ");
let result = ( num >= 100 && num <= 999 ) ? "Yes, Number("+num+") is three digit" : "No, Number("+num+") is not three digit";
console.log(result);

'''