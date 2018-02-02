from smtplib import SMTP
from email.mime.text import MIMEText
from yaml import load
from os import path
from jinja2 import Template

class Email(object):

    with open(path.dirname(path.abspath(__file__)) + '/../config/config.yml', 'r') as yml:
                config = load(yml).get('mail')

    me = config['user']

    def __init__(self):
            self.smtp = SMTP()

            print (self.config['server'])
            
            self.smtp.connect(self.config['server'], self.config['port'])
            self.smtp.ehlo()

            if self.config['env'] == 'prod':
                self.smtp.starttls()
                self.smtp.ehlo()

                self.smtp.login(self.config['user'], self.config['password'])


    def sendmail_login_senha(self):
        try:
            mail = Template(self.mensagem)

            msg = MIMEText(mail.render(senha=self.senha), 'html')

            msg.set_charset('utf-8')
            msg['From'] = self.me
            msg['To'] = self.email
            msg['Subject'] = self.subject

            self.smtp.sendmail(self.me, self.email, msg.as_string())
        except Exception as e:
            raise Exception(e)


    def __del__(self):
        self.smtp.quit()