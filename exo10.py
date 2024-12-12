word = input("Enter a word: ")
pali = True

for i in range (len(word) //2) :
    if word[i] != word[-(i+1)]:
        pali = False
    if pali == False:
        break

if pali == False:
    print("This word aint a palindrome")
else:
    print("THis word is a palindrome")