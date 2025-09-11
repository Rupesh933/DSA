# Q27. Given three numbers, print them in
# sorted order (ascending)
# int a = 9, b = 2, c = 7;
# // Output: 2 7 9

a = 9 
b = 2 
c = 7
small = a if a < b and a < c else b if b < c else c
biggest = a if a > b and a > c else b if b > c else c
second_small = (a+b+c) - (small + biggest)
print(small, second_small, biggest)
# java code 

'''
import java.util.Scanner;
class Main{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int a = 9;
        int b = 2
        int c = 7
        int smallest = (a < b && a < c) ? a : (b < c ? b : c);
        int biggest = (a > b && a > c) ? a: (b > c ? b : c);
        int second_biggest = (a + b + c) - (smallest + biggest);
        System.out.print(smallest, second_biggest, biggest)
    }

'''

# javascript code 

'''
let a = 9;
let b = 2;
let c = 7;
let small = (a < b && a < c) ? a : (b < c) ? b : c;
let biggest = (a > b && a > b) ? a : (b > c) ? b : c;
let second_biggest = (a+b+c) - (small+biggest)
console.log(small,second_biggest,biggest)

'''