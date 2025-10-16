# Q6. take a user input
# and print the difference of biggest digit
# and smallest digit of the number.
# Input:
# N=42375;
# Output:
# 5

# n = int(input('Enter a number'))
n = 42375
def is_big(n):
    big = 0
    small = 9
    while n > 0:
        digit = n % 10  # store last digit
        '''
        if digit > big:
            big = digit
        elif digit < small:
            small = digit
        '''
        big = max(big, digit)
        small = min(small, digit)

        n //= 10  # remove last digit
    print(f'Biggest no. is: {big} and small no. is: {small}')
    return big - small
print(f'Diff is: {is_big(n)}')


# java code 
'''
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        
        int result = is_big(n);   // function call
        System.out.println("Different digit is: " + result);
    }

    public static int is_big(int n) {
        int biggest = 0;
        int smallest = 9;
        while (n > 0) {
            int digit = n % 10;
            if (digit > biggest) {
                biggest = digit;
            }
            if (digit < smallest){
                smallest = digit;
            }
            n /= 10;
        }
        System.out.println("Biggest no. is: "+biggest+ " and smallest no. is "+smallest);
        return biggest-smallest;
    }
}
'''


# javascript code
'''
// n = Number(prompt("Enter a number: "))
n = 89732
let result = is_diff(n);   // function call
console.log("Different digit is: " + result);
function is_diff(n){
    let biggest = 0;
        let smallest = 9;
        while (n > 0) {
            let digit = n % 10;
            if (digit > biggest) {
                biggest = digit;
            }
            if (digit < smallest){
                smallest = digit;
            }
            n = Math.floor(n / 10);
        }
        console.log("Biggest no. is: "+biggest+ " and smallest no. is "+smallest);
        return biggest-smallest;
}
'''