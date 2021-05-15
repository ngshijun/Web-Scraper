from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import load_workbook
import datetime

theDate = str(datetime.date.today())
driver = webdriver.Chrome(executable_path=r'c:\Users\DELL\Desktop\chromedriver.exe')
driver.get('https://www.check4d.com/')
magnumResults = []
damacaiResults = []
totoResults = []
magnumResults.append(theDate)
damacaiResults.append(theDate)
totoResults.append(theDate)
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for element in soup.findAll(attrs={'id': 'magnum4d'}):
    for element1 in element.findAll(attrs={'class': 'resultTable2'}):
        for fst in element1.findAll(attrs={'class': 'resulttop'}):
            magnumResults.append(fst.text)
    for element2 in element.findAll(attrs={'class': 'resultTable2'}):
        for sAndC in element2.findAll(attrs={'class': 'resultbottom'}):
            if sAndC.text == '----':
                continue
            else:
                magnumResults.append(sAndC.text)

for element in soup.findAll(attrs={'id': 'damacai'}):
    for element1 in element.findAll(attrs={'class': 'resultTable2'}):
        for fst in element1.findAll(attrs={'class': 'resulttop'}):
            damacaiResults.append(fst.text)
    for element2 in element.findAll(attrs={'class': 'resultTable2'}):
        for sAndC in element2.findAll(attrs={'class': 'resultbottom'}):
            damacaiResults.append(sAndC.text)
damacaiResults.pop(14)

for element in soup.findAll(attrs={'id': 'sportstoto'}):
    for element1 in element.findAll(attrs={'class': 'resultTable2'}):
        for fst in element1.findAll(attrs={'class': 'resulttop'}):
            totoResults.append(fst.text)
    for element2 in element.findAll(attrs={'class': 'resultTable2'}):
        for sAndC in element2.findAll(attrs={'class': 'resultbottom'}):
            if sAndC.text == '****':
                continue
            else:
                totoResults.append(sAndC.text)

for i in range(1, len(magnumResults)):
    magnumResults[i] = int(magnumResults[i])
for i in range(1, len(damacaiResults)):
    damacaiResults[i] = int(damacaiResults[i])
for i in range(1, len(totoResults)):
    totoResults[i] = int(totoResults[i])

wb = load_workbook('MaPiao.xlsx')
m = wb['Magnum']
d = wb['DaMaCai']
t = wb['ToTo']

m.append(magnumResults)
d.append(damacaiResults)
t.append(totoResults)
wb.save('MaPiao.xlsx')

driver.close()
