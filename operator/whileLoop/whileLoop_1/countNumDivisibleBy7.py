# Q5. WAJP to print and count all the numbers from 1 to 100 which are divisible by 7.

i = 1
count = 0
while i <= 100:
    if i % 7 == 0:
        count += 1
        print(i)
    i += 1
print(count)

# java code
'''
class Main{
    public static void main(String[] args){
        int i = 1;
        int count = 0;
        while (i <= 100){
            if (i % 7 == 0){
                count ++;
            }
            i++;
        }
        System.out.println(count);
    }
}

'''

# javascript code

'''
let i = 1;
let count = 0;
while (i <= 100){
    if (i % 7 == 0){
        count ++;
    }
    i ++;
}
console.log(count);

'''