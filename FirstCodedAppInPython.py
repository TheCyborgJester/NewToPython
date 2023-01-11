#check balance
#withdraw money
#deposit money
#quit application

#option 1 check balance
#option 2  how much to withdraw
#Option 3 How much do you want to deposit
#Option 4 Print goodbye
balance = 45_275.19
def main() :
    operations = input('Hello welcome to Stealthy Banking!'
                       '\nClick 1 to Check your balance'
                       '\nClick 2 to withdraw money'
                       '\nClick 3 to deposit money'
                       '\nClick 4 to quit the application!: ')
    if operations=="1":
        print("You currently have $" + str(balance) + " in your bank account")
    elif operations=="2":
        take_money = input('How much would you like to withdraw? ')
        print("Your new balance is $",(int(balance) - int(take_money)))
    elif operations=="3":
        deposit_money = input('How much would you like to deposit? ')
        print("Your new balance is $" ,(int(balance) + int(deposit_money)))
    else:
        print("Goodbye")
        exit()
    restart = input("Would you like to go to the beginning? ").lower()
    if restart == "yes":
        main()
    else:
        print("Goodbye!")
        exit()
main()
