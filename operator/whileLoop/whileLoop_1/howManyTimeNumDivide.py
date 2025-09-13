# Q8. WAJP to print all the factors of a
# number.(number itself excluded)
# i/p: 28
# o/p: 1 2 4 7 14

num = int(input('Enter a number: '))
count = 0
i = 1 
lst = []
while i < num:
    if num % i == 0:
        lst.append(i)
        count += 1
    i += 1
print(lst)
print(count)


# java code

'''
import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        int count = 0;
        int i = 1;
        while (i < num){
            if (num % i == 0){
                System.out.print(i+ " ");
                count++;
            }
            i++;
        }
        System.out.print(count);
    }
}

'''

# javascript code
'''
let num = prompt("Enter a number");
let count = 0;
let i = 1;
while (i < num){
if (num % i == 0){
    console.log(i+ " ");
    count++
}
i++;
}
console.log(count);

'''

# Q9. WAJP to count the factors of a
#     number.(number itself excluded)
#     i/p: 28
#     o/p: Total Factors are: 5

# Q10. WAJP to print and count all the factors of
# a number.(number itself excluded)
# i/p: 28
# o/p: 1 2 4 7 14
# Total Factors are: 5