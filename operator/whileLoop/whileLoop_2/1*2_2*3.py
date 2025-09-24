# Q10. WAJP to print the sum of below series:
#      1*2 + 2*3 + 3*4 + ...... + upto 100

def printSeries(n):
    i = 1
    total = 0
    while i <= n:
        total = total + (i*i + i)   # total + (i * (i + 1))
        i += 1
    return total

n = int(input('Enter a number: '))
print(printSeries(n))



# java code
'''
import java.util.Scanner;
class Series{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int result = printSeries(n);
        System.out.print(result);
    }
    public static int printSeries(int n){
        int i = 1;
        int total = 0;
        while (i <= n){
            total = total + (i * (i+1));
            i++;
        }
        return total;
    }
}

'''

# javascript code
'''
let n = Number(prompt("Enter a number: "));
console.log(printSeries(n));

function printSeries(n){
    let i = 1;
    let total = 0;
    while (i <= n){
        total = total + (i * (i+1));
        i++;
    }
    return total;
}

'''