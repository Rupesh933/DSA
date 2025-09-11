# Q15. WAJP to check whether the given
# character is an upper case alphabet or
# not.

ch = input("Enter a single character: ")[0]  # [0] ---> agar user 'ABCD' likhta hai to ch me sirf 'A' ayega
ascii_val = ord(ch)
check = f'{ch} is in upper case' if ch  >='A' and ch <= 'Z' else f'{ch} is not in upper case'

check2 = f'{ch} ({ascii_val}) is in upper case' if ascii_val  >= 65 and ascii_val <= 90 else f'{ch} ({ascii_val}) is not in upper case'

print(check)
print(check2)


# java code

'''
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a Character");
        char num1 = sc.next().charAt(0);

        String check = (num1 >= 65 && num1 <= 90)? num1+" is in upper case" : num1+ " is not in upper case";

        System.out.println(check);
    }
}

'''

# javascript code

'''
let ch = prompt("Enter a Character: ")
let asciiVal = ch.charCodeAt(0);   // get ASCII value
let check = (asciiVal >= 65 && asciiVal <= 90)? asciiVal+" is in upper case" : asciiVal+ " is not in upper case";
console.log(check)

'''