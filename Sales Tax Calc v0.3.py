#Sales Tax Calculator v0.3
#This version implements AR, CA, CO, CT, DE, FL & GA sales tax
#Thanks to Karan for the idea
print ("Sales Tax Calculator v0.3")
print ()

while True:

    running=True
    state = input ('Please enter the state in which you are purchasing the items: ')
    if state=='AL':
        print ("Setting state to Alabama")
        print ('Please enter the total cost of all items: ')
        price = float(input())
        print ((price * 0.04) + price)
        running = False

    if state=='AK':
        print ("The state of Alaska does not have sales tax")

    if state=='AZ':
        print ("Setting state to Arizona")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.087) + price)
        running = False

    if state=='AR':
        print ("Setting state to Arkansas")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.065) + price)
        running = False

    if state=='CA':
        print ("Setting state to California")
        price = float(input ('Please enther the total cost of all items: '))
        print ((price * 0.0725) + price)
        running = False

    if state=='CO':
        print ("Setting state to Colorado")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.029) + price)
        running = False

    if state=='CT':
        print ("Setting state to Connecticut")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0635) + price)
        running = False

    if state=='DE':
        print ("The state of Delaware does not have sales tax")

    if state=='FL':
        print ("Setting state to Florida")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='GA':
        print ('Setting state to Georgia')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.04) + price)
        running = False
    
    proceed = input ('Would you like to calculate another transaction? ')
    if proceed == 'no' or proceed == 'n':
        break

print ("Goodbye")

#In version 0.4 I need to add the rest of the states
