import sys
while True:
    print('Choose an option:')
    print('     1. exit.')
    print('     2. continue')
    response = input()
    
    if response == '1':
        sys.exit()#terminate the program
        print('You typed ' + str(response) + ' to exit .')
    elif response == '2':
        #
        print('Thank you for choosing to continue, please type you name:')
        name = input()
        print('Welcome ' + name + ' ❤️ ' + ' good to see you 😊')
        break#break out of the loop
    else:
        
        
        print('Warning ⚠️ !!! You typed ' + response + ' which is not a valid ❌ response')
        print('wrong input try again ♻️')
        continue
