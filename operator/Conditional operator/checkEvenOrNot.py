# Q10. WAJP to check and print the given number
# is an even number or not.

n = int(input("Enter a number: "))
result = f"Number({n}) is Even" if n % 2 == 0 else f"Number({n}) is Odd"
print(result)


# java code
'''
import java.util.Scanner;
class checkEvenOrNot {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();   // full line input
        String result = (n % 2 == 0 ? "Number("+n+") is Even" : "Number("+n+") is Odd");
        System.out.println(result);
    }
}

'''

# javascript code
'''
let n = prompt("Enter a number");
let result = (n % 2 == 0 ? "Number("+n+") is Even" : "Number("+n+") is Odd");
console.log(result);

'''