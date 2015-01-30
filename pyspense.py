
#lists
expname = []
expcost = []
#functions go here


def addexpense():
    expensename = input('What is the name of your expense?:')
    while True:
        expenseamount = input('What is the amount of this expense? :$')
        try:
            expenseamount = float(expenseamount)
            break
        except ValueError:
            print('Please enter a number!')
    expname.append(expensename)
    expcost.append(expenseamount)
#dumb ascii splash
print(""" ____ _  _ ____ ____ ____ __ _ ____ ____ 
(  _ ( \/ / ___(  _ (  __(  ( / ___(  __)
 ) __/)  /\___ \) __/) _)/    \___ \) _) 
(__) (__/ (____(__) (____\_)__(____(____)""")
print('Welcome to PySpense v1 by G. C. Gerba')
print()
#define monthly income
print()
print('First lets find out how much you get paid and how often....')
while True:
    paycheck = input('What is your average paycheck amount?: $')
    try:
        paycheck = float(paycheck)
        break
    except ValueError:
        print('Please enter a number.')
#find out if paycheck is monthly or biweekly
while True:
    time = input('Are you paid 1 or 2 times a month? (1/2):')
    if time == '1':
        break
    elif time == '2':
        break
    else:
        print('Please enter 1 or 2')
monthlypay = float(paycheck) * int(time)
print()
print()
print()
print("OK! Now lets find out about your monthly expenses...")
print("Please add each of your expenses with a name and dollar amount.")
print('Answer no to finish adding expenses.')
#call addexpense to fill lists
while True:
    checkyn = input('Add an expense? y/n:')
    if checkyn == 'y':
        addexpense()
    elif checkyn == 'n':
        break
    else:
        print('Try Again')
#write expenses file and print list of named expenses from file
print()
print()
print("Ok! Here is a rundown of your monthly expenses. \nThis has been saved to a file called 'expenses.txt' for future reference")
print()
file1 = open('expenses.txt', 'w+')
file1.write("Here is a list of your monthly expenses...\n")
file1.write("You make $%s total a month\n" % (monthlypay))
print("Here is a list of your monthly expenses...\n")
print("You make $%s total a month\n" % (monthlypay))
for x, y in zip(expname, expcost):
    file1.write(str(x) + str(" $") + str(y) + str('\n'))
    print(str(x) + str(" $") + str(y))
file1.close()
file1 = open('expenses.txt', 'a')
totalexpcost = 0
for y in expcost:
    totalexpcost = totalexpcost + y
print("Total: $" + str(totalexpcost))
file1.write("Total: $" + str(totalexpcost))
disposable = monthlypay - totalexpcost
print('You have $%s disposable income each month' % (disposable))
file1.write("\n")
file1.write('You have $%s disposable income each month' % (disposable))
file1.close()

#todo in next version: object oriented? GUI? load already know expenses from file?
