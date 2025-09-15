# Q12. WAJP to print all the terms of Fibonacci
# series up to n.
# i/p: 7
# o/p: 0 1 1 2 3 5 8 13

def is_fibonacci(n):
    n1 = 0
    n2 = 1
    # print(f"{n1}\n{n2}")
    i = 1
    while i <= n:
        n3 = n1 + n2
        print(n1, end=" ")
        n1 = n2
        n2 = n3
        i += 1
    # return 0
is_fibonacci(7)



# java code 

'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        is_fibo(n);
    }
    public static void is_fibo(int n){
        int n1 = 0;
        int n2 = 1;
        int i = 1;
        while (i <= n){
            int n3 = n1 + n2;
            System.out.print(n1+ " ");
            n1 = n2;
            n2 = n3;
            i++;
        }
        
    }
}

'''

# javascript code

'''
let n = prompt('Enter a number to find fibonacci series: ');
n = Number(n);
is_fibo(n);
function is_fibo(n){
    let n1 = 0;
    let n2 = 1;
    let arr = []
    let i = 1;
    while (i <= n){
        arr.push(n1)
        let n3 = n1 + n2;
        n1 = n2;
        n2 = n3;
        i++;
    }
    console.log(arr.join(" "));
}

'''