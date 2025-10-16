'''
Q8. Write a java program to take a user input and print
each digit of the number from left to right.
Input:
N=43705;
Output:
4
3
7
0
5
'''

n = int(input('Enter number: '))

def left_right(n):
    n = abs(n)
    n = str(n)[::-1]
    n = int(n)
    while n > 0:
        res = n%10
        print(res)
        n //= 10

left_right(n)



# java code


# javascript code
'''
// n = Number(prompt("Enter a number: "))
let n = 43705;
let result = reversePrint(n);
console.log("reverse of " + n + " is: " + result)
function reversePrint(n) {
    let res = 0;
    let rev = 0;
    while (n > 0) {
        res = n % 10;
        rev = rev * 10 + res;
        console.log(res);
        n = Math.floor(n / 10);
    }
    return rev;
}

'''