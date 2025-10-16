# Q7. Write a java program to take a user input
# and count the total digit of the number.
# Input:
# N=43705;
# Output:
# 5

# n = int(input('Enter a number: '))
n = -43705
def count(n):
    n = abs(n)   # handle negative number
    if n == 0:
        return 1  # handle 0 case
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count 
print(f'Total number is: {count(n)}')


# java code 
'''
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        
        int result = count(n);   // function call
        System.out.println("Number of digit is: " + result);
    }

    public static int count(int n) {
        n = Math.abs(n);
        int count = 0;
        if (n == 0){
            return 1;
        }
        while (n > 0) {
            count ++;
            n /= 10;
        }
        return count;
    }
}
'''

# javascript code 
'''
// n = Number(prompt("Enter a number: "))
n = 89732
let result = count(n);   // function call
console.log("Number of digit is: " + result);
function count(n){
    n = Math.abs(n);
    let count = 0;
    if (n == 0){
        return 1;
    }
        while (n > 0) {
            count ++;
            n = Math.floor(n / 10);
        }
        return count;
    // or 
    // return String(Math.abs(n)).length;
}
'''