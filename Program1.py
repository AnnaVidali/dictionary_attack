import nacl.pwhash

file = open("hack.txt", "w")
for i in range(999):
    # asks for passwords from user001 till user009 if press y at the question below
    if i+1 < 10:
        username = 'user00' + str(i+1)
        userInput = input('Please provide password for user00' + str(i+1) + ': ')
        password = userInput.encode('utf-8')
        hashed = nacl.pwhash.str(password)
        # stores username and hashed password on txt
        file.write(username + "\t" + hashed.decode('utf-8') + "\n")
        answer = input('Do you want to continue giving passwords for users? (y,n): ')
        # continue providing passwords for users
        if answer == 'y':
            continue
        # terminates program
        elif answer == 'n':
            print('Terminating...')
            break
        # terminates program
        else:
            print('Wrong answer. Terminating...')
            break
    # asks for passwords from user011 till user100 if press y at the question below
    elif i+1 < 100:
        username = 'user0' + str(i+1)
        userInput = input('Please provide password for user0' + str(i + 1) + ': ')
        password = userInput.encode('utf-8')
        hashed = nacl.pwhash.str(password)
        # stores username and hashed password on txt
        file.write(username + "\t" + hashed.decode('utf-8') + "\n")
        answer = input('Do you want to continue giving passwords for users? (y,n): ')
        # continue providing passwords for users
        if answer == 'y':
            continue
        # terminates program
        elif answer == 'n':
            print('Terminating...')
            break
        # terminates program
        else:
            print('Wrong answer. Terminating...')
            break
    # asks for passwords from user101 till user999 if press y at the question below
    else:
        username = 'user' + str(i+1)
        userInput = input('Please provide password for user' + str(i + 1) + ': ')
        password = userInput.encode('utf-8')
        hashed = nacl.pwhash.str(password)
        # stores username and hashed password on txt
        file.write(username + "\t" + hashed.decode('utf-8') + "\n")
        answer = input('Do you want to continue giving passwords for users? (y,n): ')
        # continue providing passwords for users
        if answer == 'y':
            continue
        # terminates program
        elif answer == 'n':
            print('Terminating...')
            break
        # terminates program
        else:
            print('Wrong answer. Terminating...')
            break
file.close()