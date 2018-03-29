
#!/usr/local/bin/python3
#Import Necessary Libraries 
import tesserocr 
import pytesseract
from PIL import Image
from PIL import ImageGrab
import webbrowser
import requests
from bs4 import BeautifulSoup

#Assign the image to analyze with OCR to variable 'im'
picture = Image.open("question.jpg")

#Use method image_to_string on the variable 'im' in the language English
query = pytesseract.image_to_string(picture, lang = 'eng')

parsing = query.split("\n\n")

rawList = []
for part in parsing:
	rawList.append(part.replace('\n', ' '))

question = rawList[0]
editedList = list(rawList)
editedList.pop(0)
answers = []
for answer in editedList:
	answers.append(answer)
urls = []
for answer in editedList:
	urls.append("https://www.google.com.tr/search?q=" + question + " " + answer)

words = []
x=0 
y=0
z=0
for url in urls:
	r = requests.get(url)
	html_doc = r.text
	soup = BeautifulSoup(html_doc, 'html.parser')
	for s in soup.find_all(class_='g'):
		words.append(s.text)

for element in words:
	x = x + element.count(editedList[0])
for element in words:
	y = y + element.count(editedList[1])
for element in words:
	z = z + element.count(editedList[2])
for url in urls:
	webbrowser.open_new_tab(url)





print(x,y,z)
#toSearch = soup.get_text()




#implement method to open up tabs as secondary option 









