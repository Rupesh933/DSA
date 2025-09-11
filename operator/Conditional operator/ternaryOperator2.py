# What is the output of the program:
# int a = 3, b = 4, c = 5;
# int result = (a > b) ? (a > c ? a : c) : (b > c ? b : c);
# System.out.println(result);
# a) 3 b) 4 c) 5 d) 6

a, b, c = 3, 4, 5
result = (a if a > c else c) if a > b else (b if b > c else c)
print(result)


# java code

'''
class Profit{
    public static void main(string[] args)
    {
        int a = 3 , b = 4, c = 5;
        int result = (a > b) ? (a>c?a:c) : (b > c? b : c);
        System.out.println(result);
    }
}

'''

# javascript code
'''
let a = 3 , b = 4, c = 5;
let result = (a > b) ? (a>c?a:c) : (b > c? b : c);
console.log(result);

'''