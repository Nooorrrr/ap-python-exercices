
word = input("Word: ")
w = 30
space = (w - len(word) - 2) // 2
if len(word) % 2 != 0:
    space = space + 1

print('*' * w)
print('*' + ' ' * space+ word + ' ' * (w - len(word) - space - 2) + '*')
print('*' * w)



