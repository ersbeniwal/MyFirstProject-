#Software Developer: Sandeep Beniwal

while(1):
    print("Check Prime Number, Give Input")
    x = int(input())
    res = 0
    i = 2
    while(i < x):
        if((x % i) == 0):
            res = 1
            break
        i += 1
    if(res == 0):
        print("Prime number")
    else:
        print("Not Prime number")
    





name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')

#File Open
f = open("FilezillaServerLog.txt","r")
print(f.read())

