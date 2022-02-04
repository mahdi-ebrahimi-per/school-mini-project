with open(r"C:\Users\asus\Desktop\Chat.txt", encoding="utf8") as chat:

    previusLine = ""

    for line in list(chat.readlines()):

        # name = line[0:line.find(":")]

        # print(name)


        splitedLine = line.split()
        try:
            time = splitedLine[0]
            FirstName = splitedLine[1]
            FamilyName = splitedLine[2][0:-1]
            Name = FirstName + FamilyName
            previusLine = line

        except:
            


        print(Name)

        # break




#