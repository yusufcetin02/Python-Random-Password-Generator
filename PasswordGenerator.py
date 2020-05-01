import random

def randomPasswordGenerator(length):
    if length > 100:
        length = 100
    passwordLength = list(range(1,length+1))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                ]
    base = 1
    baseList = []
    newPassword = ''

    for i in passwordLength:
        baseList.append(i)
        base += 1

    for x in baseList:
        randomCount = random.randint(0,61)
        passwordAlphabet = alphabet[randomCount]
        newPassword += passwordAlphabet

    with open('password.txt','w') as file:
        file.write('Your Password Is : ' + newPassword)

    print(newPassword)


#while True:
#    try:
#        inputPasswordLength = input('What Is Your Password Length : ')
#        randomPasswordGenerator(int(inputPasswordLength))
#        break
#    except Exception as e:
#        print('Please enter only numbers !')
