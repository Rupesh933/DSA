# Q1. for a given number int n = 5783
# a. print the last two digit of the number
# b. Remove the last digit of the number

n = 5783
print(n%10) # 3
print(n%100) # 83
print(n//10)  # 578
print(n//100)  # 57



# java code
'''
class Digit{
    public static void main(String[] agrs){
        System.out.println("Print last digit of a number: ");
        int n = 5783;
        System.out.println(n%10);
        System.out.println(n%100);
        System.out.println(n/10);
        System.out.println(n/100);
    }
}

'''

# javascript code
'''

let n = 5783
console.log(n%10);
console.log(n%100);
console.log(Math.trunc(n/10));
console.log(Math.trunc(n/100));

'''