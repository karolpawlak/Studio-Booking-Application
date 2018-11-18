#Author: Karol Pawlak R00103090
#Description: SOFT6018 Project - Booking processing program

#constants -------------------------------------------------------------------------------------------------------------

maxNumberOfMusicians = 8

#calculating cc levy and cash reduction
#5% = 100/5 = 0.05
#Therefore to add 5% I multiply by 105% which is 1.05
#to take away 5% I multiply by 95% which is 0.95
creditCardLevy = 1.05
cashReduction = .95

#costs per day
sessionMusicianCost = 100
cost1Day = 260
cost2to4Day = 240
cost5to8Day = 210
cost9plusDay = 200

#-----------------------------------------------------------------------------------------------------------------------

#creating a file where the application output data will be saved
bookingFile = open("bookingapplication.txt", "w")

#writing the opening lines of the .txt file
bookingFile.write("Booking Application\n" + "--------------------------------------------------\n")
bookingFile.close() #closing the file so that the file does not run in the background and take up ram space

#-----------------------------------------------------------------------------------------------------------------------

#user inputing contact name for the group's manager
bookingName = input("Enter your name:>>")
while len(bookingName) < 1:
    print("ERROR - Nothing was entered.\n")
    bookingName = input("Re-enter your name:>>")
#updating the file with the name of group's manager
bookingFile = open("bookingapplication.txt", "a")
bookingFile.write("Requested by: " + str(bookingName))
bookingFile.close()

#-----------------------------------------------------------------------------------------------------------------------

#user inputing email address for contact details
emailAddress = input("Enter your email address:>>")
#i have designed three while loops which cover all invalid possibilites of email inputs
#minium number of digts in an email possible is 5 for a possiblity of x@x.xx

while len(emailAddress) < 6:
    print("ERROR - Incorrect email address - Your email is too short.\n")
    emailAddress = input("Re-enter your email address:>>")
    if "." not in emailAddress:
        print("ERROR - Incorrect email address - Please make sure your email address contains a dot.\n")
    if "@" not in emailAddress:
        print("ERROR - Incorrect email address - Please make sure your email address contains @.\n")

while "@" not in emailAddress:
    print("ERROR - Incorrect email address - Please make sure your email address contains @.\n")
    emailAddress = input("Re-enter your email address:>>")
    if "." not in emailAddress:
        print("ERROR - Incorrect email address - Please make sure your email address contains a dot.\n")
    if len(emailAddress) < 6:
        print("ERROR - Incorrect email address - Your email is too short.\n")

while "." not in emailAddress:
    print("ERROR - Incorrect email address - Please make sure your email address contains a dot.\n")
    emailAddress = input("Re-enter your email address:>>")
    if len(emailAddress) < 6:
        print("ERROR - Incorrect email address - Your email is too short.\n")
    if "@" not in emailAddress:
        print("ERROR - Incorrect email address - Please make sure your email address contains @.\n")

#updating the file with email address
bookingFile = open("bookingapplication.txt", "a")
bookingFile.write(" (Contact: " + str(emailAddress))
bookingFile.close()

#-----------------------------------------------------------------------------------------------------------------------

#user inputing phone number for contact details in format XXX-XXXXXXX
phoneNumber = input("Enter your phone number(XXX-XXXXXXX):>>")
#since all phone numbers in Ireland consist of 10 digits, i used a while loops to tell the user if the number is too short or too long
#10 digits plus 1 digit reserved for the "-" intersection
while len(phoneNumber) < 11:
    print("ERROR - The phone number you entered is too short\n")
    phoneNumber = input("Please re-enter your phone number:>>")
    if len(phoneNumber) > 11:
        print("ERROR - The phone number you entered is too long\n")
        phoneNumber = input("Please re-enter your phone number:>>")
while len(phoneNumber) > 11:
    print("ERROR - The phone number you entered is too long\n")
    phoneNumber = input("Please re-enter your phone number:>>")
    if len(phoneNumber) < 11:
        print("ERROR - The phone number you entered is too short\n")
        phoneNumber = input("Please re-enter your phone number:>>")
while phoneNumber[3] != "-":
    print("ERROR - Invalid phone number format\n")
    phoneNumber = input("Please re-enter your phone number:>>")

#boolean required for while loop to determine if phone number entirely consists of integers
phoneNumberCheck = False

while phoneNumberCheck == False:
    try:                                  #for loop that's checking every sigle digit (except [3]) if they are integers
        for phoneDigit in range(0, 11):    #using range 0 to 11 as the phone number consists of 10 digits
            if phoneDigit == 3:        #digit no 3 is the '-' that separates area code from the rest of the number
                phoneDigit += 1
            int(phoneNumber[phoneDigit])
            phoneDigit += 1
        phoneNumberCheck = True

    except:
        print("ERROR - This is not a phone number\n")
        phoneNumber = input("Please re-enter your phone number:>>")

#updating the file with phone number
bookingFile = open("bookingapplication.txt", "a")
bookingFile.write(" & " + str(phoneNumber) + ")\n\n")
bookingFile.close()

#-----------------------------------------------------------------------------------------------------------------------

#user inputing the number of band members
noOfBandMembers = input("Enter the number of band members:>>")

while len(noOfBandMembers) < 1:
    print("ERROR - Nothing was entered.\n")
    noOfBandMembers = input("Re-enter the number of band members:>>")

membersNoCheck = False #boolean to enter while loop to determine if noOfBandMembers is an integer

while membersNoCheck == False:
    try:
        if int(noOfBandMembers) <= maxNumberOfMusicians: #if the number of band members is lower than 8
            if int(noOfBandMembers) == 0: #this line covers if user still inputs a number but puts in 0 which is not possible for a number of band members
                print("ERROR - Invalid number of band members entered.\n")
                noOfBandMembers = input("Please re-enter the number of band members:>>")
            int(noOfBandMembers)
            membersNoCheck = True
        else:
            print("ERROR - This studio can only accomodate up to 8 musicians.\n") #this line covers if user inputs more than 8 musicians
            noOfBandMembers = input("Please re-enter the number of band members:>>")

    except:
        print("ERROR - This is not a number.\n")
        noOfBandMembers = input("Please re-enter the number of band members:>>")



#opening file so that the program can write the details of each band member into the file with a for loop
bookingFile = open("bookingapplication.txt", "a")
bookingFile.write("Band Members\n" + "----------------------------------\n")

members = 0 #for loop

for members in range(int(noOfBandMembers)): #using for loop to generate template for the user to input band members details  #using users input as range
    members += 1
    bandMembersName = input("What is band member #" + str(members) +"'s name?>>" )
    while len(bandMembersName) < 1:
        print("ERROR - Nothing was entered.\n")
        bandMembersName = input("Re-enter the name of band member #" + str(members) +":>>")
    bandMembersInstrument = input("What is " + str(bandMembersName) + "'s instrument?>>")
    while len(bandMembersInstrument) < 1:
        print("ERROR - Nothing was entered.\n")
        bandMembersInstrument = input("Re-enter the instrument of band member #" + str(members) +":>>")
    bookingFile.write(str(members) + ": " + str(bandMembersName) + " - " + str(bandMembersInstrument) + "\n") #overwriting the file with new data                                                                                                             #about band members

bookingFile.close() #closing the file so it doesn't run in the background

availableSessionMusicians = int(maxNumberOfMusicians) - int(noOfBandMembers) #taking away user input from max number of 8 to determine available spaces

noOfSessionMusicians = input("There is space for " + str(availableSessionMusicians) + " session musicians.\nHow many would you like?")

while len(noOfSessionMusicians) < 1:
    print("ERROR - Nothing was entered.\n")
    noOfSessionMusicians = input("Re-enter number of session mussicians requested:>>")

sessionMusiciansNoCheck = False #boolean to determine that number of session musicians entered is valid

while sessionMusiciansNoCheck == False:
    try:
        if int(noOfSessionMusicians) <= int(availableSessionMusicians): #validating that it's not higher than available number of musicians
            int(noOfSessionMusicians)
            sessionMusiciansNoCheck = True
        else:
            print("ERROR - Invalid number of session musicians entered.\n")
            noOfSessionMusicians = input("Please re-enter the number of session musicians(" + str(availableSessionMusicians) +  " available):>>")

    except:
        print("ERROR - This is not a number.\n") #error message for input not being an integer
        noOfSessionMusicians = input("Please re-enter the number of session musicians(" + str(availableSessionMusicians) +  " available):>>")
#-----------------------------------------------------------------------------------------------------------------------

#asking user to input start date in format xx/xx/xxxx
startDate = str(input("What start date are you looking for (dd/mm/yyyy):>>"))

#checking the length of the date input
while len(startDate) > 10:
    print("ERROR - Invalid date format. The date is too long.\n")
    startDate = input("Please re-enter your start date (dd/mm/yyyy):>>")
    if len(startDate) < 10:
        print("ERROR - Invalid date format. The date is too short.\n")
        startDate = input("Please re-enter your start date (dd/mm/yyyy):>>")
while len(startDate) < 10:
    print("ERROR - Invalid date format. The date is too short.\n")
    startDate = input("Please re-enter your start date (dd/mm/yyyy):>>")
    if len(startDate) > 10:
        print("ERROR - Invalid date format. The date is too long.\n")
        startDate = input("Please re-enter your start date (dd/mm/yyyy):>>")

#no backslash error check
while startDate[2] and startDate[5] != "/":
    print("ERROR - Invalid date format. Make sure you have '/' in the right place.\n")
    startDate = input("Please re-enter your start date (dd/mm/yyyy):>>")

dateCheck = False #start of the boolean that determines that user inputs digits in the right places

while dateCheck == False:
    try:
        for dateDigit in range(0,10):
            if dateDigit == 2: #digit no 2 is the backslash
                dateDigit += 1
            elif dateDigit == 5: #digit no 5 is the backslash
                dateDigit += 1
            int(startDate[dateDigit])
            dateDigit += 1
        dateCheck = True
    except:
        print("ERROR - Date does not contain numbers.\n")
        startDate = input("What start date are you looking for (dd/mm/yyyy):>>")

bookingFile = open("bookingapplication.txt", "a") #opening the file
bookingFile.write("\nDate Requested --> " + str(startDate)) #overwriting with new data
bookingFile.close()

#-----------------------------------------------------------------------------------------------------------------------

#user inputs number of days he requires to use the studio
noOfDaysRequested = input("Enter number of days you are looking for:>>")

daysRequestedCheck = False #boolean to determine whether user inputs a number

while daysRequestedCheck == False:
    try:
        if int(noOfDaysRequested) >= 1: #i use this as hardly anyone will book a studio for more than a year
            int(noOfDaysRequested)
            daysRequestedCheck = True
        elif int(noOfDaysRequested) == 0: #validates that number of days requested is not a 0
            print("ERROR - Number of days entered cannot be a 0.\n")
            noOfDaysRequested = int(input("Please re-enter number of days you are looking for:>>"))
        else:
            print("ERROR - Invalid number of days entered.\n")
            noOfDaysRequested = int(input("Please re-enter number of days you are looking for:>>"))

    except:
        print("ERROR - This is not a number.\n")
        noOfDaysRequested = input("Please re-enter number of days you are looking for:>>")

#-----------------------------------------------------------------------------------------------------------------------

#printing information for the user about payment method
print("Will you pay by:")
print("1: Credit Card (5% levy)")
print("2: Cash (5% discount)")
print("3: Cheque\n")

userChoiceCheck = False #boolean that validates that user inputs 1, 2 or 3

userChoice = 0
paymentType = ""

while userChoiceCheck == False:
    try:
        userChoice = int(input("Enter your choice here(1, 2 or 3):>>"))
        if userChoice == 1: #option 1 = credit card
            paymentType = "Credit Card"
            userChoiceCheck = True
        elif userChoice == 2: #option 2 = cash
            paymentType = "Cash"
            userChoiceCheck = True
        elif userChoice == 3: #option 3 = cheque
            paymentType = "Cheque"
            userChoiceCheck = True
        else:
            print("ERROR - Invalid choice entered. Make sure you enter 1, 2 or 3.\n")
    except:
        print("ERROR - This is not a number. Make sure you enter 1, 2 or 3.\n")

#-----------------------------------------------------------------------------------------------------------------------

#calculating the total price for the booking
#data needed:
#-session mucicians cost
#-base cost multiplied by number of session musicians inputed by the user
#-if user selected cash, add 5% from total cost
#-if user selected card, take away 5% from total cost
#-if user selected cheque, leave the total cost as it is

totalSessionMusiciansCost = int(noOfSessionMusicians) * sessionMusicianCost #user input multiplied by 100

costByDays = 0
totalCost = 0

if int(noOfDaysRequested) == 1:
    costByDays = int(noOfDaysRequested) * cost1Day #user input multiplied by 260
elif int(noOfDaysRequested) >= 2 and int(noOfDaysRequested) <= 4:
    costByDays = int(noOfDaysRequested) * cost2to4Day #user input multiplied by 240
elif int(noOfDaysRequested) >= 5 and int(noOfDaysRequested) <= 8:
    costByDays = int(noOfDaysRequested) * cost5to8Day #user input multiplied by 210
elif int(noOfDaysRequested) >= 9:
    costByDays = int(noOfDaysRequested) * cost9plusDay #user input multiplied by 200

if userChoice == 1:
    totalCost = (costByDays + totalSessionMusiciansCost) * creditCardLevy
elif userChoice == 2:
    totalCost = (costByDays + totalSessionMusiciansCost) * cashReduction
elif userChoice == 3:
    totalCost = costByDays + totalSessionMusiciansCost

#-----------------------------------------------------------------------------------------------------------------------
#updating the file with final data

bookingFile = open("bookingapplication.txt", "a")
bookingFile.write("\nIncludes " + str(noOfSessionMusicians) + " session musicians per day.\n")
bookingFile.write("Payment will be €" + format(totalCost, '.2f') + " to be paid by " + str(paymentType) + ".")
bookingFile.close()

#-----------------------------------------------------------------------------------------------------------------------

#let's print out the entire thing so that user can see his booking application

bookingFile = open("bookingapplication.txt")
print("\n\n") #two lines to separate the previous recent output so it looks more neat and is easier to read
print(bookingFile.read()) #printing the entire bookingapplication.txt