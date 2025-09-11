# Q:1 int a = 5, b = 10;
# int c = (a > b) ? a++ : b++;
# System.out.println(a + " " + b + " " + c);
# a) 5 11 5 b) 6 10 6
# c) 5 11 10 d) 6 11 10
a = 5
b = 10
c = a+1 if a>b else b+1
print(c)


# java code
'''
class Profit{
    public static void main(string[] args)
    {
        int a = 5;
        int b = 10
        int c = (a>b) ? a++ : b++;
        System.out.println(c);
    }
}

'''

# javascript code
'''
let a = 5;
let b = 10;
let c = (a>b) ? a++ : b++;
console.log(c)
'''