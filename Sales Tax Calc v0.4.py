#Sales Tax Calculator v0.4
#This version implements Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine sales tax
#Thanks to Karan for the idea
print ("Sales Tax Calculator v0.4")
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

    if state=='HI':
        print ('Setting state to Hawaii')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.04) + price)
        running = False

    if state=='ID':
        print ('Setting state to Idaho')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='IL':
        print ('Setting state to Illinois')
        price = float(input ('PLease enter the total cost of all items: '))
        print ((price * 0.0625) + price)
        running = False

    if state=='IN':
        print ('Setting state to Indiana')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='IA':
        print ('Setting state to Iowa')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='KS':
        print ('Setting state to Kansas')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.065) + price)
        running = False

    if state=='KY':
        print ('Setting state to Kentucky')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='LA':
        print ('Setting state to Louisiana')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0445) + price)
        running = False

    if state=='ME':
        print ('Setting state to Maine')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.055) + price)
        running = False
                      
    proceed = input ('Would you like to calculate another transaction? ')
    if proceed == 'no' or proceed == 'n':
        break

print ("Goodbye")

#In version 0.5 I need to add more ways to enter state names, abbreviations
