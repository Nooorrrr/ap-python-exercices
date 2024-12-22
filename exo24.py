def anagrams(word1,word2):
    return sorted(word1) == sorted(word2)


while True:
    word1 = input("Enter the first word (enter 'quit' to quit): ")
    if word1 == "quit":
        break
    word2 = input("Enter the second word: ")
    if anagrams(word1,word2):
        print("The words are anagrams")
    else:
        print("The words are not anagrams")
    print("----------------------------")