#Software Developer: Sandeep Beniwal

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

