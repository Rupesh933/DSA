# Q13. find sum of all even numbers upto n without loop
# n = 100
# 2+4+6+.....+upto 100
# o/p = 2550

n = 100
sum_even = (n//2)*((n//2)+1)
print(sum_even)


# java code
'''
class Profit{
    public static void main(string[] args)
    {
        int n = 100;
        int sum_even = ((n/2)*((n/2)+1));
        System.out.println("sum of all even number of " +n+ " is: "+sum_even);
    }
}

'''

# javascript code

'''
let n = 100;
let sum_even = Math.trunc((n/2)*((n/2)+1));
console.log("sum of all even number of " +n+ " is: "+sum_even);

'''