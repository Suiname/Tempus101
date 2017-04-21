carousel = ["Elle", "Diego", "Jason"]

for number in range(2 * len(carousel)):
    if (number % 2 == 0):
        print('still spinning')
    else:
        print(carousel[number / 2]);
