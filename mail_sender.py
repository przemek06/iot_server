import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import Config

class MailSender:
    instances = {}

    @classmethod
    def add_instance(cls, id, encoder):
        cls.instances[id] = encoder

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]

    def __init__(self):
        self.email_address = Config.read_property("email_address")
        self.password = Config.read_property("email_password")

    def send_recharge_info_mail(self, email, uid, price):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = email
            msg['Subject'] = "You account has been charged"

            html = """\
            <html>
            <head></head>
            <body>
                <p>Hello!<br>
                Your account has been charged due to purchases on your Public Transpord Card - UID: {}. The amount of debited funds is {} zł.
                </p>
                <p>Thank you for using our services!</p>
            </body>
            </html>
            """.format(uid, price)

            body = MIMEText(html, 'html')
            msg.attach(body)

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(self.email_address, self.password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())

            server.quit()
            print("Mail sent correctly")
        except Exception as e:
            print(e)
            


