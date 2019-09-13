from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from bs4 import BeautifulSoup
import requests
import os

url = os.environ.get('url')
target_price = os.environ.get('target_price')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

s = requests.Session()

r = s.get(url, headers=headers)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'lxml')

data = {}

# Getting Product title from the page
product_title = soup.select_one('#productTitle').text.strip()

# Finding all thumbnail selections of available options
items = soup.findAll('li')

# Iterating through each option example: color, size etc
for item in items:
    # Getting the title of the option
    if item.get('title'):
        # Cleaning up title and price
        title = item.get('title').replace('Click to select ', '')
        try:
            price = float(item.find(class_='twisterSwatchPrice').text.replace('$', '').strip())
        except AttributeError:
            price = item.find(class_='olpMessageWrapper').text.replace('from', 'Available from ').strip()
        data[title] = price

final_list = ''
for k, v in data.items():
    final_list += f'<br>{k} = ${v}'


def send_mail(low_price):
    message = Mail(
        from_email=('support@razains.com', 'My Deals'),
        to_emails='syedrazatx@gmail.com',
        subject=f'[Deal Alert] for {product_title}',
        html_content=f'<strong>{product_title}</strong><br><br><strong>Lowest Price: </strong>${low_price}<br>{final_list}')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


lowest_price = min([value for value in data.values() if isinstance(value, float)])
if lowest_price < float(target_price):
    send_mail(lowest_price)
else:
    pass
