[![Python 3.7](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/downloads/release/python-374/)

# Amazon Price Alert
Script that emails price alerts for a given item on Amazon.com



#### Usage

- Script can be deployed on a Raspberry Pi 
  - Uses `FLASK` as a server
  - Uses `SendGrid` to send the email alerts
  - Can use `.env` or system defined environment variables



##### The script requires the following environment variables

| Environment Variable Name | Example                                                      | Notes                                                        |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| url                       | https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_2?dchild=1&keywords=playstation+5&qid=1603840297&sr=8-2 | Direct URL to the item that you want to set the alert for    |
| target_price              | 399.00                                                       | Price that will trigger the alert email                      |
| EMAIL_FROM                | example@example.com                                          | The email sender for the alert email                         |
| EMAIL_TO                  | example@example.com                                          | The email that will receive the price alert. Can be a comma separated list of emails |
| SENDGRID_API_KEY          | *API key*                                                    | API key from [SendGrid](https://sendgrid.com/)               |

