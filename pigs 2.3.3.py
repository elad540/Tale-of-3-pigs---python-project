print('The Tale of "The Three Little Pigs" tells us about three pigs who lived under the threat of a wolf. \nIn order to provide themselves with shelter from him, they began to gather together building materials.')

print()
number = int (input('Enter 3 digits, each digit represents the number of bricks collected by one of the piggies-  '))
print()
print('The total number of bricks collected by the piggies:  ')
print(int(int(number / 100) + int((number % 100) / 10) + int((number % 100) % 10)))

print()
print('The number of bricks that each pig will get if they divide the total number of bricks is equal between them:')
print(int(int(number / 100) + int((number % 100) / 10) + int((number % 100) % 10)//3))

print()
print('The remainder after dividing the bricks:')
print(int(int(number / 100) + int((number % 100) / 10) + int((number % 100) % 10)%3))

print()
print('If the amount is divided between the three pigs without a remainder:')
print(int((int(int(number / 100) + int(number / 10) % 10 + number % 10) / 3)))

print()
input('Press Enter  to exit')
