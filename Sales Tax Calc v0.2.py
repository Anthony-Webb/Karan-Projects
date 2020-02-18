#Sales Tax Calculator v0.2
#This version implements AL, AK, AZ sales tax
#Thanks to Karan for the idea
print ("Sales Tax Calculator v0.2")
print ()

while True:

    running=True
    state = input ('Please enter the state in which you are purchasing the items: ')
    if state=='AL':
        print ("Setting state to Arizona")
        print ('Please enter the total cost of all items: ')
        price = int(input())
        print ((price * 0.04) + price)
        running = False

    if state=='AK':
        print ("The state of Alaska does not have sales tax")

    if state=='AZ':
        print ("Setting state to Arizona")
        price = int(input ('Please enter the total cost of all items: '))
        print ((price * 0.087) + price)
        running = False

    proceed = input ('Would you like to calculate another transaction? ')
    if proceed == 'no' or proceed == 'n':
        break

print ("Goodbye")
