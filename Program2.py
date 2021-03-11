import nacl.pwhash

# creates txt to write down users and their cracked passwords
file3 = open("results.txt", "w")

with open("hack.txt", "r") as file1:
    for line1 in file1:
        with open("popularpasswords.txt", "r") as file2:
            for line2 in file2:
                try:
                    # verifies if the hashed password and the password are the same
                    result = nacl.pwhash.verify(line1.strip('\n').split('\t')[-1].encode('utf-8'), line2.strip('\n').encode('utf-8'))
                    print("It's a Match! The password for user: " + line1.strip('\n').split('\t')[0] + " is: " + line2.strip('\n') + ". Saving password...")
                    # stores username of user and password that has been cracked
                    username = line1.strip('\n').split('\t')[0]
                    password = line2.strip('\n')
                    file3.write(username + "\n" + password + "\n")
                    print('Password has been saved!')
                except:
                    continue
# closes all files that have been uses
file1.close()
file2.close()
file3.close()
