

word = input("Please type in a word :")
if len(word)!= 1:
    print(f"There are {len(word)} letters in the word {word} Thank you!")
else :
    print("Thank you")

print("------------------------------------------------------------------")

def even_uneven(num):
    if int(num)%2 == 1:
        return "uneven"
    else :
        return "even"

num = input("ara numero :")
print(f"the number is {even_uneven(num)}")

print("-------------------------------------------------------------------")

print("wsh sa7bi kifash  jaz lmatch :")
baranya = int(input("aaa lbaranya markaw :"))
lhouma = int(input("w 7na l7ouma markina : "))

if lhouma == baranya :
    print("aaaa it was a tie mala")
elif lhouma > baranya :
    print("sa7aaaa lhouma rb7to ")
else:
    print("aaaaa madernash, 9oltelkom 3aytouli ndirlkom gardien")








    