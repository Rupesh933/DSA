# Q6. WAJP to print and count all the numbers from 1 to 100 which are divisible by 7 or ends with 7.

count = 0
i = 1
while i <= 100:
    if i % 7 == 0 or i % 10 == 7:
        print(i)
        count += 1
    i += 1
print(count)

# java code

'''
class Main{
    public static void main(String[] args){
        int count = 0;
        int i = 1;
        while (i <= 100){
            if (i % 7 == 0 || i % 10 == 7){
                System.out.println(i);
            }
            i++;
        }
        System.out.println(count);
    }
}
'''

# javascript code

'''
let count = 0;
let i = 1;
while (i <= 100){
if (i % 7 == 0 || i % 10 == 7){
    System.out.println(i);
}
i++;
}
System.out.println(count);

'''

# Q7. WAJP to print and count all the numbers
#     from 1 to 1000 which are divisible by 7
#     and also ends with 7.