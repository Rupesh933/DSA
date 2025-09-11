# Q8. find the last digit of a number without using % operator.
# intput = 12345
# o/p --> 5
n = 12345
last_digit = n - (n // 10) *10   # (n//10) --> 1234, (n//10)*10 --> 12340, n - 12340 --> 5
print(f'last digit of {n} is:  {last_digit}')

# java code 
'''
class Profit{
    public static void main(string[] args)
    {
        int n = 12345;
        int last_digit = n/10;
        last_digit = last_digit * 10;
        last_digit = n - last_digit;
        System.out.println("last digit of "+n+ " is "+last_digit);
    }
}
'''

# javascript code
'''
let n = 12345;
let last_digit = Math.trunc(n / 10);
last_digit = last_digit * 10;
last_digit = n -last_digit;
console.log("last digit of "+n+ " is "+last_digit);

'''