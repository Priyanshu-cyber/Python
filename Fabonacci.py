num = int(input("Enter the nth term till you want to calculate fabonacci series: \n"))
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a+b
    return a
ls= []
for i in range(1, num+1):
    ls.append(f(i))
print("Fabonacci series till ",num, "is :")
print(ls)
result = sum(ls)
print(result)
print(f"Sum of fabonacci series is {result}")