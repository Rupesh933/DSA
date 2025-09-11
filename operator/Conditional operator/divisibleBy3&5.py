# Q12.WAJP to check and print the given
# number is divisible by both 3 and 5 or
# only by 3, only by 5 or None.

num = 20
check = f"no.{num} is divisible both 3 & 5 " if num%3==0 and num%5==0 else f'no.{num} only divisible by only 3' if num%3==0 else f'no.{num} is divisble by only 5'
print(check)


# java code

'''
import java.util.Scanner;
class check {
    public static void main(String[] args)
    {
       Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();   // full line input
        String result = ( num%3 == 0 && num%5==0 ) ? "Number("+num+") is divisible by both" : (num%3==0) ? "Number("+num+") is only divisible by 3" : "Number("+num+") is only divisible by 3";
        System.out.println(result);
    }
}

'''

# javascript code

'''
let num = prompt('Enter a number: ')
result = ( num%3 == 0 && num%5==0 ) ? "Number("+num+") is divisible by both" : (num%3==0) ? "Number("+num+") is only divisible by 3" : "Number("+num+") is only divisible by 3";
console.log(result);

'''