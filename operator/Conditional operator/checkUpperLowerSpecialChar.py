# Q18. Given a character, check if it's uppercase,
# lowercase, digit or special character.

ch = input('Enter a character: ')[0]
check = f'{ch} is in uppercase' if ch >= 'A' and ch <= 'Z' else f'{ch} is in lowercase' if ch >= 'a' and ch <= 'z' else f'{ch} is digit' if ch >= '0' and ch <= '9' else f'{ch} is special character'
print(check)



# java code

'''
import java.util.Scanner;
class Main{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a char: ");
        char ch = sc.next().charAt(0);
        String check = ch >= 65 && ch <= 90 ? ch+" is in uppercase" : ch >= 97 && ch <= 122 ? ch+" is in lowercase" : ch >= 48 && ch <= 57 ? ch+" Character is digit" : ch+ " is Special character";
        System.out.println(check);
    }
}

'''

# javascript code

'''
let ch = prompt('Enter a char value: ')
let asciiVal = ch.charCodeAt(0);   // get ASCII value
let check = asciiVal >= 65 && asciiVal <= 90 ? ch+" is in uppercase" : asciiVal >= 97 && asciiVal <= 122 ? ch+" is in lowercase" : asciiVal >= 48 && asciiVal <= 57 ? ch+" Character is digit" : ch+ " is Special character";
console.log(check);

'''
