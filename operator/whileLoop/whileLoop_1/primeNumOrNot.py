# Q11. WAJP to print a number is prime number or not.
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print(f'{n} is a  prime number')
else:
    print(f'{n} is not a prime number')


# java code
'''
import java.util.Scanner;
class Main{
    public static void main(String[] agrs){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        if (is_prime(n)){
            System.out.print(n+ " is a prime number");
        }
        else{
            System.out.print(n+ " is not a prime number");
        }
    }
    public static boolean is_prime(int n){
        if (n < 2){
            return false;
        }
        int i = 2;
        while (i*i <= n){     // Sirf sqrt(n) tak loop
            if (n % i == 0){   // Factor mil gaya
                return false;    //  Prime nahi hai
            }
            i++;
        }
        return true;    // Koi factor nahi mila → Prime hai
    }
}

'''

# javascript code

'''
function is_prime(n){
    n = Number(n);  // ensure number
    if (n < 2){
        return false;
    }
    let i = 2;
    while (i*i <= n){
        if (n % i == 0){
            return false;
        }
        i++;
    }
    return true;
}

let n = prompt("Enter a number: ")
if (is_prime(n)){
    console.log(n+ " is a prime number");
}
else{
    console.log(n+ " is not a prime number");
}

'''