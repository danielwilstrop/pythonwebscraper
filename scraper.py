import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.co.uk/Apple-iPad-Air-10-9-inch-Wi-Fi-64GB/dp/B08J66Z99G/ref=sr_1_1_sspa?dchild=1&keywords" \
      "=ipad+air&qid=1626695174&sr=8-1-spons&psc=1&spLa" \
      "=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyODdGR1QwS1k2NzRWJmVuY3J5cHRlZElkPUEwMDUzODA4WUM3VEZZUDFPWkFIJmVuY3J5cHRlZEFkSWQ9QTA2Nzg3NjQzTVVYSEhJTThWUTJKJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== "

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/91.0.4472.164 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle')

print(title)


