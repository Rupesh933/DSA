# Q25. Print if a year is a leap year or NOT using
# only conditional operator.
'''
Leap Year Rules
1). Agar year 400 se divisible hai → leap year.

2). Agar year 100 se divisible hai lekin 400 se nahi → not a leap year.

3). Agar year 4 se divisible hai lekin 100 se nahi → leap year.

4). Otherwise → not a leap year.

'''

year = int(input("Enter year to check leap year or not: "))
check = f'{year} is leap year' if year % 400 == 0 or year % 100 != 0 and year % 4 == 0 else f'{year} is not a leap year'
print(check)


# java code 

'''
import java.util.Scanner;
class Main{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a year: ");
        int year = sc.nextInt();
        String check = (year % 400 == 0 || year % 100 != 0 && year % 4 == 0) ? year+" is leap year" : year+ " not leap year";
        System.out.print(check);
    }
}

'''

# javascript code 
'''
let year = prompt('Enter year: ')
let check = (year % 400 == 0 || year % 100 != 0 && year % 4 == 0) ? year+" is leap year" : year+ " not leap year";
console.log(check)

'''