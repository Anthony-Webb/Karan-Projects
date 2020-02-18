#Sales Tax Calculator v0.6
#This version implements the sales tax for the rest of the states.
#Thanks to Karan for the idea
print ("Sales Tax Calculator v0.6")
print ()

while True:

    running=True
    state = input ('Please enter the state in which you are purchasing the items: ')
    if state=='AL' or state=='al' or state=='Alabama' or state=='alabama':
        print ("Setting state to Alabama")
        print ('Please enter the total cost of all items: ')
        price = float(input())
        print ((price * 0.04) + price)
        running = False

    if state=='AK' or state=='ak' or state=='Alaska' or state=='alaska':
        print ("The state of Alaska does not have sales tax")
        running = False

    if state=='AZ' or state=='az' or state=='Arizona' or state=='arizona':
        print ("Setting state to Arizona")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.087) + price)
        running = False

    if state=='AR' or state=='ar' or state=='Arkansas' or state=='arkansas':
        print ("Setting state to Arkansas")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.065) + price)
        running = False

    if state=='CA' or state=='ca' or state=='California' or state=='california':
        print ("Setting state to California")
        price = float(input ('Please enther the total cost of all items: '))
        print ((price * 0.0725) + price)
        running = False

    if state=='CO' or state=='co' or state=='Colorado' or state=='colorado':
        print ("Setting state to Colorado")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.029) + price)
        running = False

    if state=='CT' or state=='ct' or state=='Connecticut' or state=='connecticut':
        print ("Setting state to Connecticut")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0635) + price)
        running = False

    if state=='DE' or state=='de' or state=='Delware' or state=='delaware':
        print ("The state of Delaware does not have sales tax")

    if state=='FL' or state=='fl' or state=='Florida' or state=='florida':
        print ("Setting state to Florida")
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='GA' or state=='ga' or state=='Georgia' or state=='georgia':
        print ('Setting state to Georgia')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.04) + price)
        running = False

    if state=='HI' or state=='hi' or state=='Hawaii' or state=='hawaii':
        print ('Setting state to Hawaii')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.04) + price)
        running = False

    if state=='ID' or state=='id' or state=='Idaho' or state=='idaho':
        print ('Setting state to Idaho')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='IL' or state=='il' or state=='Illinois' or state=='illinois':
        print ('Setting state to Illinois')
        price = float(input ('PLease enter the total cost of all items: '))
        print ((price * 0.0625) + price)
        running = False

    if state=='IN' or state=='in' or state=='Indiana' or state=='indiana':
        print ('Setting state to Indiana')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='IA' or state=='ia' or state=='Iowa' or state=='iowa':
        print ('Setting state to Iowa')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='KS' or state=='ks' or state=='Kansas' or state=='kansas':
        print ('Setting state to Kansas')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.065) + price)
        running = False

    if state=='KY' or state=='ky' or state=='Kentucky' or state=='kentucky':
        print ('Setting state to Kentucky')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='LA' or state=='la' or state=='Louisiana' or state=='louisiana':
        print ('Setting state to Louisiana')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0445) + price)
        running = False

    if state=='ME' or state=='me' or state=='Maine' or state=='Maine':
        print ('Setting state to Maine')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.055) + price)
        running = False

    if state=='MD' or state=='md' or state=='Maryland' or state=='maryland':
        print ('Setting state to Maryland')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='MA' or state=='ma' or state=='Massachusetts' or state=='massachusetts' or state=='Mass' or state=='mass':
        print ('Setting state to Massachusetts')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0625) + price)
        running = False

    if state=='MI' or state=='mi' or state=='Michigan' or state=='michigan':
        print ('Setting state to Michigan')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='MN' or state=='mn' or state=='Minnesota' or state=='minnesota':
        print ('Setting state to Minnesota')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06875) + price)
        running = False

    if state=='MS' or state=='ms' or state=='Mississippi' or state=='mississippi':
        print ('Setting state to Mississippi')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='MO' or state=='mo' or state=='Missouri' or state=='missouri':
        print ('Setting state to Missouri')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.04255) + price)
        running = False

    if state=='MT' or state=='mt' or state=='Montana' or state=='montana':
        print ('The state of Montana does not have sales tax')

    if state=='NE' or state=='ne' or state=='Nebraska' or state=='nebraska':
        print ('Setting state to Nebraska')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.055) + price)
        running = False

    if state=='NV' or state=='nv' or state=='Nevada' or state=='nevada':
        print ('Setting state to Nevada')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0685) + price)
        running = False

    if state=='NH' or state=='nh' or state=='New Hampshire' or state=='new hampshire':
        print ('The state of New Hampshire does not have sales tax')

    if state=='NJ' or state=='nj' or state=='New Jersey' or state=='new jersey':
        print ('Setting state to New Jersey')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06625) + price)
        running = False

    if state=='NM' or state=='nm' or state=='New Mexico' or state=='new mexico':
        print ('Setting state to New Mexico')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.05125) + price)
        running = False

    if state=='NY' or state=='ny' or state=='New York' or state =='new york':
        print ('Setting state to New York')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.045) + price)
        running = False

    if state=='NC' or state=='nc' or state=='North Carolina' or state=='north carolina':
        print ('Setting state to North Carolina')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0475) + price)
        runing = False

    if state=='ND' or state=='nd' or state=='North Dakota' or state=='north dakota':
        print ('Setting sate to North Dakota')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.05) + price)
        running = False

    if state=='OH' or state=='oh' or state=='Ohio' or state=='ohio':
        print ('Setting state to Ohio')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0575) + price)
        running = False

    if state=='OK' or state=='ok' or state=='Oklahoma' or state=='oklahoma':
        print ('Setting state to Oklahoma')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.045) + price)
        running = False

    if state=='OR' or state=='or' or state=='Oregon' or state=='oregon':
        print ('The state of Oregon does not have sales tax')
        running = False
        
    if state=='PA' or state=='pa' or state=='Pennsylvania' or state=='pennsylvania' or state=='Penn' or state=='penn':
        print ('Setting state to Pennsylvania')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='RI' or state=='ri' or state=='Rhode Island' or state=='rhode island' or state=='Rhode' or state=='rhode':
        print ('Setting state to Rhode Island')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='SC' or state=='sc' or state=='South Carolina' or state=='south carolina':
        print ('Setting state to South Carolina')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='SD' or state=='sd' or state=='South Dakota' or state=='south dakota':
        print ('Setting state to South Dakota')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.045) + price)
        running = False

    if state=='TN' or state=='tn' or state=='Tennessee' or state=='tennessee':
        print ('Setting state to Tennessee')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='TX' or state=='tx' or state=='Texas' or state=='texas':
        print ('Setting state to Texas')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0625) + price)
        running = False

    if state=='UT' or state=='ut' or state=='Utah' or state=='utah':
        print ('Setting state to Utah')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.0485) + price)
        running = False

    if state=='VT' or state=='vt' or state=='Vermont' or state=='vermont':
        print ('Setting state to Vermont')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='VA' or state=='va' or state=='Virginia' or state=='virginia':
        print ('Setting state to Virginia')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.043) + price)
        running = False

    if state=='WA' or state=='wa' or state=='Washington' or state=='washington':
        print ('Setting state to Washington')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.07) + price)
        running = False

    if state=='WV' or state=='wv' or state=='West Virginia' or state=='west virginia':
        print ('Setting state to West Virginia')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.06) + price)
        running = False

    if state=='WI' or state=='wi' or state=='Wisconsin' or state=='wisconsin':
        print ('Setting state to Wisonsin')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.05) + price)
        running = False

    if state=='WY' or state=='wy' or state=='Wyoming' or state=='wyoming':
        print ('Settiny state to Wyoming')
        price = float(input ('Please enter the total cost of all items: '))
        print ((price * 0.04) + price)
        running = False
        
    proceed = input ('Would you like to calculate another transaction? ')
    if proceed == 'no' or proceed == 'n':
        break

print ("Goodbye")

#In version 0.7 I need to add sales tax for in all variatons, but first need to learn how states "do" sale taxes/
