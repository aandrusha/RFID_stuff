
# coding: utf-8

# In[1]:

# Программа конвертирует код смарт-карты EM-Marin в формат для программаторов TMD-5 и аналогичных (5 октетов, первые 2 - 09 00)
import sys
import warnings
warnings.filterwarnings("ignore")
print ("Введи код с карты в формате 123/45678")
DecNumberList = list(str(input()))
i = 0
FirstPart, MidPart, LastPart = "", "", ""

while i < len(DecNumberList):
    try:
        n = int(DecNumberList[i])
    except ValueError:
        break
    FirstPart = FirstPart + DecNumberList[i]
    i += 1

try:
    MidPart = DecNumberList[i]
except IndexError:
    sys.exit("Во введённом коде отсутствует разделитель")


i += 1
while i < len(DecNumberList):
    try:
        n = int(DecNumberList[i])
    except ValueError:
        break
    LastPart = LastPart + DecNumberList[i]
    i += 1    
print (str('0900')+str(hex(int(FirstPart)))[2:]+str(hex(int(LastPart)))[2:])


# In[ ]:



