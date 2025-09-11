# Q12. find sum of all odd numbers up to n without loop
# no = 100
# 1+3+5+....+upto 100
# o/p = 2500
n = 100
sum_odd = (n//2)**2
print(sum_odd)


# java code

'''
class Profit{
    public static void main(string[] args)
    {
        int n = 100;
        int count = (n +1) /2;
        int sum_odd = count * count;
        System.out.println(sum_odd);
    }
}

'''


# javascript code
'''
let n = 100
let count = Math.trunc((n+1)/2);
let sum_odd = count * count;
console.log(sum_odd);

'''