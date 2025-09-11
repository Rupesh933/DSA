# Q16. WAJP to check whether the given
# character is an lower case alphabet or
# not.

ch = input("Enter a single character: ")[0]  # [0] ---> agar user 'ABCD' likhta hai to ch me sirf 'A' ayega
ascii_val = ord(ch)
check = f'{ch} is in upper case' if ch  >='a' and ch <= 'z' else f'{ch} is not in upper case'

check2 = f'{ch} ({ascii_val}) is in upper case' if ascii_val  >= 97 and ascii_val <= 122 else f'{ch} ({ascii_val}) is not in upper case'

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

        String check = (num1 >= 95 && num1 <= 122)? num1+" is in upper case" : num1+ " is not in upper case";

        System.out.println(check);
    }
}

'''

# javascript code

'''
let ch = prompt("Enter a Character: ")
let asciiVal = ch.charCodeAt(0);   // get ASCII value
let check = (asciiVal >= 95 && asciiVal <= 122)? asciiVal+" is in upper case" : asciiVal+ " is not in upper case";
console.log(check)

'''