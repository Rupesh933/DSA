# Q13. print the sum of below series: 1/1 + 1/2 + 1/3 + 1/4 ..... +upto 100

def series(n):
    total = 0
    i = 1
    while i <= n:
        total += 1/(i)
        i += 1
    return total

n = int(input("Enter a number: "))
print(series(n))

# Q14. print the sum of below series: 1/2 + 1/4 + 1/6 + 1/8 ..... + upto 100

def series(n):
    total = 0
    i = 1
    while i <= n:
        total += 1/(i*2)
        # total += 1/(i*2+1)  for odd series 1/3 + 1/5 + 1/7 + 1/9 ..... + upto 100
        i += 1
    return total

# n = int(input("Enter a number: "))
print(series(n))

