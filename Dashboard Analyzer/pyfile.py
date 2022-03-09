# Packages
# import requests
import pymsgbox as window
import os
import re
import logging
import time


#log
logging.basicConfig(filename='Log/App.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s : %(message)s - %(process)d')


# main
StartMainButtons = ["ثبت نمرات", "نمایش نمرات"]
operation = window.confirm(text="Select a operation : ", title='', buttons=StartMainButtons)

if operation == None:
    quit()



dir_list = os.listdir("Classes")
for directory in dir_list:
    if os.path.isdir(f"Classes/{directory}"):
        continue

    else:
        window.alert("Unable class format", title="Error", button="ok")
        logging.error("Unable class format")
        quit()


Selected_class= window.confirm(text="Select a Class : ", title='', buttons=dir_list)

if Selected_class == None:
    quit()


# Find Newest Html file
try:
    max = 0
    dir_list = os.listdir("Classes/"+Selected_class)
    for file in dir_list:
        if "html" not in file:
            continue
        
        time = os.path.getmtime(f"Classes/{Selected_class}/{file}")

        if time > max:
            max = time
            newest_htmlFile = file


except:
    window.alert(text="There is no Defined class", title="Error", button="Ok")
    logging.error("There is no Defined class")
    quit()


#_____________________

# Load Content
try:
    path = f"Classes/{Selected_class}/{newest_htmlFile}"

    with open(path, encoding="utf-8") as f:
        content = ""
        i = 0
        for line in f:
            
            i += 1

            if i == 24:
                content = line

except:
    window.alert(text=f"There is no HTML file (Dashboard tahlily) in {Selected_class} Class", title="Error", button="Ok")
    logging.error(f"There is no HTML file (Dashboard tahlily) in {Selected_class} Class")
    quit()


def Extract(content, startAttribute, endAttribute=None, LenForEndAttribute=None ):
    startIndexes = [_.start() for _ in re.finditer(startAttribute, content)]

    if endAttribute and LenForEndAttribute:
        raise ValueError("you cant get value to endAttribute and LenForEndAttribute both")

    elif endAttribute:
        result = []
        for index in startIndexes:
            pharse_start = index+len(startAttribute)
            end = content[pharse_start:].find(endAttribute)
            pharse = content[pharse_start:pharse_start+end].replace("\u200c", " ")
            result.append(pharse)

        return result

    elif LenForEndAttribute:
        result = []
        for index in startIndexes:
            pharse_start = index+len(startAttribute)
            result.append(content[pharse_start:pharse_start+LenForEndAttribute])



def SpliteContent(content, SplitAttr):
    splited_content = []
    startIndexes = [_.start() for _ in re.finditer(SplitAttr, content)]

    i = 0
    for index in startIndexes:
        if i < (len(startIndexes)):
            # 0 to -2
            try:
                splited_part = content[startIndexes[i]: startIndexes[i+1]]
                splited_content.append(splited_part)
                i += 1
            # -1 to end
            except:
                splited_part = content[startIndexes[i]:]
                splited_content.append(splited_part)
                
    return splited_content



def IsExistenceInListPerItem(List, string):
    existence = []
    for item in List:
        if string in item:
            existence.append(True)

        else:
            existence.append(False)

    return existence




# specific function fot this program
def ExsistAttr_ValueNone(content, SpliteAttribute, DesireAttribute):
    splitedContent = SpliteContent(content, SpliteAttribute)
    speakedOrNot = IsExistenceInListPerItem(splitedContent, DesireAttribute)

    Value_None = []

    index = 0
    for part in splitedContent:
        if speakedOrNot[index]:
            Time = Extract(part, DesireAttribute, "<")
            Value_None.append(Time[0])
            index += 1

        else:
            Value_None.append(None)
            index += 1

    return Value_None





# date تاریخ
attr = "mt-3 col-text-right py-1 text-gray-500 inline-block\"><p class=\"font-bold\"><div class=\"inline\">"
date = Extract(content, attr, "<")

# Names نام ها
names = Extract(content, "xl:max-w-sm max-w-xs\">", "<")

# online duration زمان آنلاین بودن
attr = "\"M5.636 18.364a9 9 0 010-12.728m12.728 0a9 9 0 010 12.728m-9.9-2.829a5 5 0 010-7.07m7.072 0a5 5 0 010 7.07M13 12a1 1 0 11-2 0 1 1 0 012 0z\"></path></svg> "
online_duration = Extract(content, attr, "<br>")

# speaking time زمان صحبت کردن
NameAttr = "xl:max-w-sm max-w-xs\">"
SpeakAttr = "\"M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z\"></path></svg> "
speakingTime = ExsistAttr_ValueNone(content, NameAttr, SpeakAttr) 

# Camera time زمان دوربین دادن
NameAttr = "xl:max-w-sm max-w-xs\">"
CamTime = "M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z\"></path></svg> "
cameraTime = ExsistAttr_ValueNone(content, NameAttr, CamTime)


# Messages پیام ها 
NameAttr = "xl:max-w-sm max-w-xs\">"
ChatAttr = "M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z\"></path></svg> "
NumOfChat = ExsistAttr_ValueNone(content, NameAttr, ChatAttr)

# Raise Hand دست بلند کردن
NameAttr = "xl:max-w-sm max-w-xs\">"
RaiseHand = "M7 11.5V14m0-2.5v-6a1.5 1.5 0 113 0m-3 6a1.5 1.5 0 00-3 0v2a7.5 7.5 0 0015 0v-5a1.5 1.5 0 00-3 0m-6-3V11m0-5.5v-1a1.5 1.5 0 013 0v1m0 0V11m0-5.5a1.5 1.5 0 013 0v3m0 0V11\"></path></svg> "
NumOfHand = ExsistAttr_ValueNone(content, NameAttr, RaiseHand)

#_________

# make Activity Archive of does not exist
dir_list = os.listdir(f"Classes")
for Class in dir_list:
    files = os.listdir(f"Classes/{Class}")
    path = os.path.join(f"Classes/{Class}", "Activity Archive")
    mode = 0o666
    if "Activity Archive" not in files:
        os.mkdir(path, mode)


try:
    dir_list = os.listdir(f"Classes/{Selected_class}/Activity Archive")
    files = []
    standard_date = date[0].replace(" ", "")
    for file in dir_list:
        file = file.replace(" ", "")[:-4]
        files.append(file)

    if standard_date not in files:    
        index = 0
        for person in names:
            with open(f"Classes/{Selected_class}/Activity Archive/{date[0]}.txt", "a+", encoding="utf-8") as out:
                out.write(f"{names[index]}|{online_duration[index]}|{speakingTime[index]}|{cameraTime[index]}|{NumOfChat[index]}|{NumOfHand[index]}\n")

            index+=1
    
        window.alert("Done!", "Ok", "Ok")

    else:
        window.alert(text="You added this meeting befor", title="Alert", button="Ok")



except:
    window.alert(text="Error in write in meeting archive", title="Error", button="Ok")
    logging.error("Error in write in meeting archive")



# تغییر ضرایب هنوز کامل نشده

# # Load indicators
# try:
#     indicators = []
#     dir_list = os.listdir("Settings")

#     if "indicators.txt" in dir_list:
#         with open("Settings/indicators.txt", 'r') as inds:
#             for ind in inds:
#                 indicators.append(int(ind))

#     else:
#         open("Settings/indicators.txt", 'w').close()

#     if len(indicators) < 5 :
#         window.alert(text="Length of indicators must be 5", title="Error", button="Ok")
#         logging.error("Error in Load indicators")
#         quit


# except:
#     window.alert(text="Error in Load indicators", title="Error", button="Ok")
#     logging.error("Error in Load indicators")








# Read data
# with open(f"Classes/{Selected_class}/{date[0]}.txt", "r", encoding="utf-8") as file:
#     for i in file:
#         print(i.split('|'))




    

