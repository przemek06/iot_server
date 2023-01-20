from mqqt_queue import Queue
from database import Database
from mail_sender import MailSender
import msvcrt

def main():
    queue = Queue()
    Queue.add_instance("queue", queue)
    database = Database()
    Database.add_instance("database", database)
    mail_sender = MailSender()
    MailSender.add_instance("mail_sender", mail_sender)

    working = True
    print("Press E to close the program")

    while working:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8") 
            if key == "e":
                working = False

    print("Finished execution")

if __name__ == "__main__":
    main()