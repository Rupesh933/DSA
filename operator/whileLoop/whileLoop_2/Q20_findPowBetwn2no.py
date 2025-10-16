# Q20. WAJP to accept two numbers from user
# and print power of a to b.
# i/p: 6 3
# o/p: 6 to power 3 is: 216

print(6**3)
def power(base, expo):
    total = 1
    i = 1
    while i <= expo:
        total *= base
        i += 1
    return total
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(power(a,b))



# java code 
'''
class Main {
    public static void main(String[] args) {
        int base = 6;
        int exp = 3;
        double result = Math.pow(base, exp);  // returns double
        System.out.println(result);  // 216.0
    }
}
or 

int result = (int) Math.pow(6, 3);
System.out.println(result);  // 216

'''

# javascript code 
'''
console.log(6 ** 3);  // 216
'''