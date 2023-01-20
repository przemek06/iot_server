import paho.mqtt.client as mqtt
from config import Config
import json
from database import Database
from mail_sender import MailSender

class Queue:

    instances = {}

    @classmethod
    def add_instance(cls, id, encoder):
        cls.instances[id] = encoder

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]
    
    def __init__(self) -> None:
        mqtt.Client.connected_flag=False
        self.client = mqtt.Client("12r234fdsfft3g34gyuh896ry") 
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        host = Config.read_property("broker_host")
        port = Config.read_property("port")
        username = Config.read_property("adafruit_user")
        key = Config.read_property("adafruit_key")
        self.client.username_pw_set(username, password=key)
        self.client.connect(host, port=port)   
        self.client.loop_start()
        self.topic = Config.read_property("topic")

    def on_message(self, client, userdata, msg):
        value = msg.payload.decode("utf-8")
        try:
            message_json = json.loads(value)
            uid = message_json["uid"]  
            price = message_json["price"]      
            database = Database.get_instance("database")
            email_row = database.find_email_by_uid(uid)
            print(email_row)

            if email_row is None:
                return
            
            email = email_row[0]
            mail_sender = MailSender.get_instance("mail_sender")
            mail_sender.send_recharge_info_mail(email, uid, price)

        except Exception as e:
            print(e)
    
    def on_connect(self, client, userdata, flags, rc):
        if rc==0:
            client.connected_flag=True
            print("Connected OK")
            topic = Config.read_property("topic")
            client.subscribe(topic, qos=0)

        else:
            print("Bad connection Returned code=",rc)