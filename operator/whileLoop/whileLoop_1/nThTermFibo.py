# Q13. WAJP to print the nth term of Fibonacci
#      series.
#      i/p: 7
#      o/p: 13

def nth_fibo(n):
    n1 = 0
    n2 = 1
    i = 1
    while i <= n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i += 1
    # print(n1, end=" ")
    return n1

n = int(input('Enter a number to find nth term fibonacci series: '))
result = nth_fibo(n)
print(f'The {n}th fibonacci series number is: {result}')


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
        int n3 = n1+n2;
        n1 = n2;
        n2 = n3;
        i++;
    }
    System.out.print(n1+ " ");
}
}
'''

# javascript code

'''
let n = prompt('Enter a number to find nth term of fibonacci series: ');
is_fibo(n);

function is_fibo(n){
    let n1 = 0;
    let n2 = 1;
    let i = 1;
    while (i <= n){
        let n3 = n1 + n2;
        n1 = n2;
        n2 = n3;
        i++;
    }
    console.log(n1);
}

'''