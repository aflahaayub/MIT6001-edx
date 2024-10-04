num = int(input("Input the number: "))
binary = ""
if num < 0:
    num = abs(num)
if num == 0:
    binary = str(num)
while num > 0:
    binary = str(num%2) + binary
    num = num//2
print(binary)