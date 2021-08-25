# expenses = [10.50,8,5,15,20,5,3]
# total = sum(expenses)

# # #add the total of list
# # for x in expenses:
# #     sum = sum + x


# print("You spent $" , total, " on lunch this week.", sep = '')

#Another way of adding items to list
#range allows to iterate a certain number of times
expenses = []

#User can input number of expenses which will be the number of iterations
#Loop will do
num_expenses= int(input("Enter # of expenses:" ))

for x in range(num_expenses):
    expenses.append(float(input("Enter an expense:\n")))
    total = sum(expenses)

print("You spent $" , total, " on lunch this week.", sep = '') 
print(expenses)


