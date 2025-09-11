# Q11. find sum of N natural numbers without loop
# n = 100 
# o/p = 5050
# 1+2+3+......+upto 100
n = 100
sum = n*(n+1)//2
print(f'sum of n natural number of {n} is: {sum}')



# java code
'''
class Profit{
    public static void main(string[] args)
    {
        int n = 100;
        int sum = n*(n+1)/2;
        System.out.println("sum of n natural number of "+n+ " is: "+sum);
    }
}

'''

# javascript code
'''
let n = 100
let sum = Math.trunc(n*(n+1)/2)
console.log("sum of n natural number of "+n+ " is: "+sum)

'''