# Q3. to swap two number
# with using a third variable
# without using third variable
a = 10 
b = 20 
temp = a   # temp = 10
a = b     # a = b --> 20
b = temp   # b = temp --> 10
print(f'a: {a} \n b: {b}')
a = 10 
b = 20
a = a+b  # 10+20 --> 30
b = a-b  # 30-20 --> 10
a = a-b  # 30-10 --> 20
print(f'a: {a} \n b: {b}')


# java code

'''
class Digit{
    public static void main(String[] agrs){
        System.out.println("swap number number: ");
        // Method 1: Swapping using a temporary variable
        int a = 10, b = 20;
        int temp = a;
        a = b;
        b = temp;
        System.out.println(a+ "\n" +b);
         // Method 2: Swapping using arithmetic operations
        a = 10;
        b = 20;
        a = a+b;
        b = a-b;
        a = a-b;
        System.out.println(a+ "\n" +b);
    }
}

'''

# javascript code
'''

let a = 10 , b = 20;
let temp = a;
a = b;
b = temp;
console.log(a+ "\n" +b);
a = 10;
b = 20;
a = a+b
b = a-b
a = a-b
console.log(a+ "\n" +b)

'''

# Q4. for the given three numbers. swap 1st into 2nd and 3rd into 1st number. 
#     a). with using fourth variable
#     b). without using fourth variable
first = 10
second = 20
third = 30
fourth = first
first = second
second = third
third = fourth
print('with using fourth variable')
print(f'first: {first}, second: {second}, third: {third}') # 20 30 10
print('without using fourth variable')
first, second, third = 10, 20, 30

# swap first <-> second
first = first + second
second = first - second
first = first - second

# swap second <-> third
second = second + third
third  = second - third
second = second - third
print(f'first: {first}, second: {second}, third: {third}')

# java code
'''
class Digit{
    public static void main(String[] agrs){
        System.out.println("swap number number: ");
        int first = 10;
        int second = 20;
        int third = 30;
        int fourth = first;
        first = second;
        second = third;
        third = fourth;
        System.out.println(first+ "\n" +second+ "\n" +third); // 20 30 10
         // Method 2: Swapping using arithmetic operations
        first = 10;
        second = 20;
        third = 30;
        first = first+second;
        second = first-second;
        first = first - second;

        second = second + third;
        third = second - third;
        second = second- third;
        System.out.println(first+ "\n" +second+ "\n" +third)

    }
}

'''

# javascript code
'''

let first = 10;
let second = 20;
let third = 30;
let fourth = first;
first = second;
second = third;
third = fourth;
console.log(first+ "\n" +second+ "\n" +third);

first = 10;
second = 20;
third = 30;

first = first + second;
second = first - second;
first = first - second;

second = second + third;
third = second - third;
second = second - third;
console.log(first+ "\n" +second+ "\n" +third);

'''