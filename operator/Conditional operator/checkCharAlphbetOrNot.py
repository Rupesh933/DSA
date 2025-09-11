# Q17. WAJP to check whether the given
# character is an alphabet or not.

ch = input('Enter a Character: ')[0]
check = f'{ch} is alphabet' if ch not in 'aeiou' else f'{ch} is vowel'
print(check)


import java.util.Scanner;
class Main{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a char: ");
        char ch = sc.next().charAt(0);
        String check = ch == 'A' || 'E' || 'I' || O' || 'U' || 'a' || 'e' || 'i' || 'o' || 'u' ? ch+ " is vowel" : ch+ " is alphbet";
        System.out.println(check);
    }
}