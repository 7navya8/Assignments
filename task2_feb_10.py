# print the no is odd or even 
# odd_even.py
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
# print number from 10 to 1
# countdown.py
for i in range(10, 0, -1):
    print(i)
# sum until user stops:keep asking the user to enter numbers and calculate the sum
# stop only when the user enters 0
# sum_until_zero.py
total = 0
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    total += n

print("Final Sum =", total)