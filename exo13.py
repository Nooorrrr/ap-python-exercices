dash =""
string =" "

while string !="":
    string = input("Please type in a string (or leave it empty if u want to stop): ")
    for i in range(len(string)):
        dash = dash +"-"
    print(string)
    print(dash)
    dash = ""
