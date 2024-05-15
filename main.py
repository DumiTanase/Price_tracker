from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.co.uk/Instant-Pot-Electric-Pressure-Stainless/dp/B00OP26T4K/ref=sr_1_4?crid=3TSJEAMJZU1D7&dib=eyJ2IjoiMSJ9.OcFL4PBvLpJp37-eJLpM7sZZ7D99MXoR8ifpY6Lf6UTaV5eUOSxcjXe3iSoKqrJotJs1N_IsafQBYwqeAmgHZ3wht_yJ2Uq1VI1Ocx7yeoxrVAChcpNriTr6XHhRnc-mlvEYXa-8Z6nNLLyTsXnysie_GOcd2F-ZniW4kARWGLwFE1Oj-PwuhVRfbA4IZmu-BbsMB02ilT_IK09suLa8Ywc8SYglOGwrhdjQgHJFAXU.Tbktc7T2ppZoOcaEN1fQj_L6WoVCyMBxVJ9NE0UMTNM&dib_tag=se&keywords=hot%2Bpot%2Bcooker&qid=1713204407&sprefix=hot%2Bpot%2Caps%2C73&sr=8-4&th=1"
headers = {"Accept-Language" : "en,ro;q=0.9,it;q=0.8,es;q=0.7",
           "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
response = requests.get(URL, headers=headers)
html_text = response.text
soup = BeautifulSoup(html_text, "lxml")

price_initial = (soup.find(name="span", class_="a-price-whole")).get_text()
# decimal = (soup.find(name="span", class_="a-price-fraction")).get_text()
price = int(price_initial.replace(".", ""))


password ="password"
my_email = "email"

if price < 100:
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg="Subject: Price Alert\n\nHellooo")