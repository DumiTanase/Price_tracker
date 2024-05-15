from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.co.uk/Instant-Pot-Electric-Pressure-Sterilizer/dp/B083KM6BZS/ref=sr_1_7?dib=eyJ2IjoiMSJ9.Y9nCxgV7efdzlufj63DqY2ihtVGQE18krUGhY5_o6lvJzFPqNeDX0gFtcVmXthSxJuvRYD4HgQhi3oAVe_bM6YLpA3CF0ezKmFwIjPQe4X5LF-1E1574jADvT4JYQHNOJXn2PEOpRPa9TdRvRG9eCS5eYkQ7d4VD222VjIX-T289eoE-_V8N7ifxmeVVm_58zyFg7MFXbfyohTBo5MLJDAF6lnE4GNc51DcIVusHxzuIaSxv2lgcmscKHMgTEQm01gtPY3yQM4LIY-5ZXQ6fUPvj4kkq9U7inA91iB78e1c.JYoyEDQXeqKHLFhGKWzegxmENFw80djxe2ATlZ_jgFo&dib_tag=se&keywords=instant%2Bpots&qid=1715792979&sr=8-7&th=1"
headers = {"Accept-Language" : "en,ro;q=0.9,it;q=0.8,es;q=0.7",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
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
                            msg="Subject: Price Alert\n\n Instant Pot Price below 100")
