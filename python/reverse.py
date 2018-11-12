# num=int(input("Enter the number:"))
# reversed=0
# rem=0

# while(num>0):
#         rem = num%10
#         reversed = reversed*10 + rem
#         num //= 10

# print(reversed)


def reverse(n):
    rev=0
    rem=0
  
    while(n>0):
        rem = n%10
        rev = rev*10 + rem
        n //= 10

    return rev


num=int (input("Enter the number"))
result = reverse(num);
print(result)
    