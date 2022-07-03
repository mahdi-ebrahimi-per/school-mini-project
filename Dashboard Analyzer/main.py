import pymsgbox as window
import os
import re
import logging
import time
from datetime import time


class ContinuousActivity():
    
    def __init__(self):
        self.Log()
        self.guiWindow()
        
        
    
    def Log(self) -> None:
        logging.basicConfig(filename='Log/App.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s : %(message)s - %(process)d')
        
    
    def guiWindow(self):
        StartMainButtons = ["ثبت نمرات فایل متنی", "نمایش نمرات"]
        operation = window.confirm(text="Select a operation : ", title='', buttons=StartMainButtons)
        return operation    
        

    
    def timeProcces(self, time1, time2) -> str:
        def FarsiNumsToEnglish(num):
            if type(num) == str:
                farsi = "۰۱۲۳۴۵۶۷۸۹"
                english = "0123456789"
                index = 0
                for i in range(10):
                    num = num.replace(farsi[index], english[index])
                    index += 1

                return num


            elif type(num) == list:
                result = []
                for item in num:
                    # print(FarsiNumsToEnglish(item), type(item))
                    result.append(FarsiNumsToEnglish(item))
                    # print(result)
            
                return result

            return num

        def Time2Secend(time):
            result = ((int(time.hour) * 3600) + int(time.minute) + int(time.second))
            return result

        def divideTwoTimes(a, b):
            a = Time2Secend(a)
            b = Time2Secend(b)
            return a/b



        time1 = FarsiNumsToEnglish(time1).split(":")[1:]
        time2 = FarsiNumsToEnglish(time2).split(":")[1:]

        time1 = time(0, int(time1[0]), int(time1[1]))
        time2 = time(0, int(time2[0]), int(time2[1]))

        return divideTwoTimes(time2, time1)


    
main = ContinuousActivity()
# a = main.timeProcces("00:30:00", "00:15:00")
# print(a)
