# Q5. for the given CP and SP. calculate %profit
CP = 120
SP = 160
if SP > CP:
    profit = SP - CP
    print(f'There is Profit: {profit}') # There is Profit: 40
    profit_per = (profit/CP) * 100
    print(f'Profit%: {profit_per}')  # Profit%: 33.33333333333333

# java code

'''
class Profit{
    public static void main(string[] args)
    {
        System.out.println("Calculate profit %: ");
        int CP = 120;
        int SP = 160;
        if (SP > CP){
            int profit = SP - CP;
            System.out.println("There is Profit: "+profit);  //There is Profit: 40
            float profit_per = ((float)profit/CP)*100;
            System.out.println("Profit%: " +profit_per);   // Profit%: 33.33333333333333
        }
    }
}

'''

# javascript code
'''
let CP = 120;
let SP = 160;
if (SP > CP)
{
    let profit = SP - CP;
    console.log('There is Pofit: '+profit);    // There is profit: 40
    let profit_per = (profit/CP)*100;
    console.log("Profit%: "+profit_per);     // Profit%: 33.33333333333333
}
'''

# Q6. for the given CP and SP. calculate %loss.
#     CP = 120
#     SP = 90
CP = 120
SP = 90
if CP > SP:
    loss = CP - SP
    print(f'There is loss: {loss}')  # There is loss: 30
    loss_per = (loss/CP)*100
    print(f'loss%: {loss_per}')  # loss%: 25.0


# java code
'''
class Loss{
    public static void main(string[] args)
    {
        System.out.println("Calculate loss %: ");
        int CP = 120;
        int SP = 90;
        if (CP > SP){
            int loss = CP - SP;
            System.out.println("There is Profit: "+loss);  //There is loss: 30
            float loss_per = ((float)loss/CP)*100;
            System.out.println("loss%: " +loss_per);   // loss%: 25.0
        }
    }
}
'''

# javascript code
'''
let CP = 120;
let SP = 90;
if (CP > SP)
{
    let loss = CP - SP
    console.log("There is loss: "+loss);    // There is loss: 30
    let loss_per = (loss/CP)*100;
    console.log("loss%: "+loss_per);   // loss%: 25
}
'''