def check_even(n):
    if n%2==0:
        return 1
    else:
        return 0
a=check_even(10)
if a==1:
    print("Even number")
else:
    print("Odd number")