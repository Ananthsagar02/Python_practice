print('Hello world!')

# input = int(input("enter a number: "))

# if (input % 2==0) and input > 10:
#     print(f"{input} is an even number")
# else:
#      print(f"{input} is an odd number")


#message = f"{input} is an even number" if input % 2 ==0 else f"{input} is an odd number"
# print(message)

#   for loop

expense = [100, 200, 300, 400, 500, 1200]
len(expense)

total_expense = 0
for item in expense:
     print(f"item is {item}")
     total_expense = total_expense + item
print(f"total expense is {total_expense}")

total_expense = 0
for i, exp in enumerate(expense):
     print(f"{i + 1} item is {exp}")
     total_expense = total_expense + exp
print(f"total is {total_expense}")