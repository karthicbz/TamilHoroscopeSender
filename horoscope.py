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
	#sl is source language and I set it to auto
	#tl is target language which I set it to Tamil(ta)
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
#	s.login("your_email_id", "your_password")
#	message = message.encode('utf-8').strip()
#	s.sendmail("your_emailid", "receiver_email", message)
#	s.quit()

def sendMessage(message, number):
	account_sid = "Your_sid"
	auth_token = "your_token"
	client = Client(account_sid, auth_token)
	msg = client.messages.create(body=message, from_='your_number', to=number)
	print("Id: "+msg.sid+"/nMessage sent to: "+number)

horoList = [['12', 'person_number'],['3', 'person_number'],['11', 'person_number']]
url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign='
for i in range(0, len(horoList)):
	message = translate(parseUrl(url+horoList[i][0]))
#password = input("Enter your passowrd:")
	sendMessage(message, horoList[i][1])
