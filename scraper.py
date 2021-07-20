import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.co.uk/Apple-iPad-Air-10-9-inch-Wi-Fi-64GB/dp/B08J66Z99G/ref=sr_1_1_sspa?dchild=1&keywords" \
      "=ipad+air&qid=1626695174&sr=8-1-spons&psc=1&spLa" \
      "=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyODdGR1QwS1k2NzRWJmVuY3J5cHRlZElkPUEwMDUzODA4WUM3VEZZUDFPWkFIJmVuY3J5cHRlZEFkSWQ9QTA2Nzg3NjQzTVVYSEhJTThWUTJKJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== "

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/91.0.4472.164 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[1:7])

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #Use own email and password here
    server.login(#username, #password)

    subject = "Ipad is cheap!"
    body = 'Link below for iPad air, price had fallen below £500  ' \
           ' "https://www.amazon.co.uk/Apple-iPad-Air-10-9-inch-Wi-Fi-64GB/dp/B08J66Z99G/ref=sr_1_1_sspa?dchild=1&keywords" \
      "=ipad+air&qid=1626695174&sr=8-1-spons&psc=1&spLa" \
      "=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyODdGR1QwS1k2NzRWJmVuY3J5cHRlZElkPUEwMDUzODA4WUM3VEZZUDFPWkFIJmVuY3J5cHRlZEFkSWQ9QTA2Nzg3NjQzTVVYSEhJTThWUTJKJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'daniel.wilstrop@outlook.com',
        'daniel.wilstrop@outlook.com',
        msg
    )

if(converted_price < 600):
    send_mail()
    print("Mail Sent")




