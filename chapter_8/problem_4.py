# fahrenteit 

# sum(n) = 1 + 2 + 3 + 4..... n-1 + n
# sum(n) = sum(n-1) + n

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))