# Q14. find sum of squares of all naturals upto n without loop
# n = 100
# 1^2 + 2^2 + 3^2 + 4^2+ ...... upto 100
# o/p = 338350

n = 100
sum_sqare = ((n*(n + 1)*(2*n + 1)) // 6)
print(f'Sum of sqares of all naturals number of {n} is {sum_sqare}')

# java code
'''
class Profit{
    public static void main(string[] args)
    {
        int n = 100;
        int sum_sqare = ((n*(n+1)*(2*n+1)) / 6);
        System.out.println("Sum of sqares of all naturals numbers of "+n+ " is: "+sum_sqare);
    }
}

'''

# javascript code
'''
let n = 100;
let sum_sqare = Math.trunc((n*(n+1)*(2*n+1)) / 6);
console.log("Sum of sqares of all naturals numbers of "+n+ " is: "+sum_sqare);

'''