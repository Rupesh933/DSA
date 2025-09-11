# Q9. Reverse 3 digit number using pure arithmetic operator
# input = 123
# o/p = 321
n = 123
m = n
last_digit1 = n % 10 # --> 123 % 10 = 3
n = n // 10   # 123 // 10 = 12
last_digit2 = n % 10 # 12 % 10 = 2
n = n // 10  # 12 // 10 = 1
reverse = last_digit1*100 + last_digit2*10+n
print(f'reverse of {m} is: {reverse}')



# java code 

'''
class Profit{
    public static void main(string[] args)
    {
        System.out.println("Calculate profit %: ");
        int n = 12345;
        int m = n;
        int last_digit1 = n%10;  // --> 5
        n = n / 10;  // --> 1234
        int last_digit2 = n % 10;  // --> 4
        n = n / 10;  // --> 123
        int last_digit3 = n % 10; // --> 3
        n = n / 10;   // --> 12
        int last_digit4 = n % 10;  // --> 2
        n = n / 10;   // --> 1
        int reverse = last_digit1*10000 + last_digit2*1000 + last_digit3*100 + last_digit4*10 + n;
        System.out.println("reverse of "+m+ " is: "+reverse);
    }
}

'''

# javascript code
'''
// In JS, / does floating-point division (not integer like Java/Python).
let n = 12345;
let m = n;
let last_digit1 = n%10;  // --> 5
n = Math.trunc(n / 10);  // --> 1234
let last_digit2 = n % 10;  // --> 4
n = Math.trunc(n / 10);  // --> 123
let last_digit3 = n % 10; // --> 3
n = Math.trunc(n / 10);   // --> 12
let last_digit4 = n % 10;  // --> 2
n = Math.trunc(n / 10);   // --> 1
reverse = last_digit1*10000 + last_digit2*1000 + last_digit3*100 + last_digit4*10 + n
console.log("reverse of "+m+ " is: "+reverse);

'''