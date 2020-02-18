#Sales Tax Calculator v0.5
#This version implements the sales tax for the rest of the states.
#Thanks to Karan for the idea
print ("Sales Tax Calculator v0.5")
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

    if state=='MD':
        print ('Setting state to Maryland')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='MA':
        print ('Setting state to Massachusetts')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0625) + price)
        running = False

    if state=='MI':
        print ('Setting state to Michigan')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='MN':
        print ('Setting state to Minnesota')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06875) + price)
        running = False

    if state=='MS':
        print ('Setting state to Mississippi')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='MO':
        print ('Setting state to Missouri')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.04255) + price)
        running = False

    if state=='MT':
        print ('The state of Montana does not have sales tax')

    if state=='NE':
        print ('Setting state to Nebraska')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.055) + price)
        running = False

    if state=='NV':
        print ('Setting state to Nevada')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0685) + price)
        running = False

    if state=='NH':
        print ('The state of New Hampshire does not have sales tax')

    if state=='NJ':
        print ('Setting state to New Jersey')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06625) + price)
        running = False

    if state=='NM':
        print ('Setting state to New Mexico')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.05125) + price)
        running = False

    if state=='NY':
        print ('Setting state to New York')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.045) + price)
        running = False

    if state=='NC':
        print ('Setting state to North Carolina')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0475) + price)
        runing = False

    if state=='ND':
        print ('Setting sate to North Dakota')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.05) + price)
        running = False

    if state=='OH':
        print ('Setting state to Ohio')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0575) + price)
        running = False

    if state=='OK':
        print ('Setting state to Oklahoma')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.045) + price)
        running = False

    if state=='OR':
        print ('The state of Oklahoma does not have sales tax')
        running = False
        
    if state=='PA':
        print ('Setting state to Pennsylvania')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='RI':
        print ('Setting state to Rhode Island')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='SC':
        print ('Setting state to South Carolina')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='SD':
        print ('Setting state to South Dakota')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.045) + price)
        running = False

    if state=='TN':
        print ('Setting state to Tennessee')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='TX':
        print ('Setting state to Texas')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0625) + price)
        running = False

    if state=='UT':
        print ('Setting state to Utah')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0485) + price)
        running = False

    if state=='VT':
        print ('Setting state to Vermont')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='VA':
        print ('Setting state to Virginia')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.043) + price)
        running = False

    if state=='WA':
        print ('Setting state to Washington')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='WV':
        print ('Setting state to West Virginia')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='WI':
        print ('Setting state to Wisonsin')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.05) + price)
        running = False

    if state=='WY':
        print ('Settiny state to Wyoming')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.04) + price)
        running = False
        
    proceed = input ('Would you like to calculate another transaction? ')
    if proceed == 'no' or proceed == 'n':
        break

print ("Goodbye")

#In version 0.6 I need to add more ways to enter state names, abbreviations
