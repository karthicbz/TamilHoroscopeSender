import requests
from bs4 import BeautifulSoup
import smtplib
from twilio.rest import Client

def parseUrl(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    mainData = soup.find_all('div',{'class':'tablet-ad'})
    for data in mainData:
        return(data.contents[1].find_all('p')[0].text)

def translate(text):
	r = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=ta&dt=t&q='+text)
	horoscopeText = r.json()
	text = ""
	#print(len(horoscopeText[0]))
	for i in range(0, len(horoscopeText[0])):
		text += horoscopeText[0][i][0]
	return text

#def sendMail(message):
#	s = smtplib.SMTP('smtp.gmail.com', 587)
#	s.starttls()
#	s.login("pkarthicbz@gmail.com", "Karthickflash123&$")
#	message = message.encode('utf-8').strip()
#	s.sendmail("pkarthicbz@gmail.com", "pspk0302@gmail.com", message)
#	s.quit()

def sendMessage(message, number):
	account_sid = "AC5b07d087ef1dfeed878bd5ac4ccabaf0"
	auth_token = "3e7a4c6fdf5ffdc659dae0662eb774d0"
	client = Client(account_sid, auth_token)
	msg = client.messages.create(body=message, from_='+12564884531', to=number)
	print("Id: "+msg.sid+"/nMessage sent to: "+number)

horoList = [['12', '+918072840660'],['3', '+919790744131'],['11', '+916381358227']]
url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign='
for i in range(0, len(horoList)):
	message = translate(parseUrl(url+horoList[i][0]))
#password = input("Enter your passowrd:")
	sendMessage(message, horoList[i][1])
