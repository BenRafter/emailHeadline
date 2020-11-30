import smtplib, ssl
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")

holderString=""

for news in news_list:
    holderString=holderString + news.title.text+ "\n"
    holderString=holderString + news.pubDate.text+"\n"
    holderString=holderString + news.link.text+"\n"
    holderString=holderString + ("-"*60) + "\n"
    
port = 465
smtpServer = "smtp.gmail.com"
password = "Add password here"
senderEmail = "Add sender email here"
recieverEmail = "Add reciever email here"
context = ssl.create_default_context()
message="""\
Subject: Here are your news headlines

"""

message=message+holderString
message=message.encode('utf-8')

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(senderEmail, password)
    server.sendmail(senderEmail, recieverEmail, message)
    