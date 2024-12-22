unique_words =[]


while True:
    word= input("Enter a unique word (enter 'quit' to quit): ")
    if word == "quit":
        break

    if word in unique_words:
        print("The word is not unique")
        print("the number of unique words is: ", len(unique_words))
        print("--------------------")
        break
    else:
        unique_words.append(word)
        print("The word has been added to the list")
        