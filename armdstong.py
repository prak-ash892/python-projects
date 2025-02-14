#armstron no b/w 1 to 500:
for num in range(1,500):
    n=num
    d3=n%10
    n=int(n/10)
    d2=n%10
    n=int(n/10)
    d1=n%10
    n=int(n/10)
    if d1**3+d2**3+d3**3==num:
        print(num)
