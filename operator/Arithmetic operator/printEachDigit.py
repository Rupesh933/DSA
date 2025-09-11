# Q2. for a given number int n = 5783
#   print each digit of the number one by one
# 3 --> 8 --> 7 --> 5
n = 5783
print(n%10) # 3
print(n)   # 5783
n//=10 # n = n // 10 --> 5783 // 10 = 578
print(n%10) #  8
n //= 10  # n = n// 10 --> 578 // 10 = 57
print(n%10) # 7
n //= 10
print(n%10) # 5

# java code

'''
class Digit{
    public static void main(String[] agrs){
        System.out.println("Print each digit of the number: ");
        int n = 5783;
        System.out.println(n%10);
        n /= 10;
        System.out.println(n%10);
        n /= 10;
        System.out.println(n%10);
        n /= 10;
        System.out.println(n%100);
    }
}

o/p --> 3875
'''

# javascript code

'''

let n = 5783
console.log(n%10);
n /= 10;
console.log(Math.trunc(n%10));
n /= 10;
console.log(Math.trunc(n%10));
n /= 10;
console.log(Math.trunc(n%10));

'''