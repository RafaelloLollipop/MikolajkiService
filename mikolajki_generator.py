import random
import smtplib

class MikolajkiGenerator(object):
    def __init__(self, participants):
        self.participants = participants

    def make_lottery(self):
        self.make_backup_message("Starting Lottery\n")
        lottery_matchs = self.chose_chosen_one()
        self.send_emails_to_users(lottery_matchs)

    def send_emails_to_users(self, lottery_matchs):
        for match in lottery_matchs:
            user = match[0]
            user_chosen_one = match[1]
            self.send_email(user, user_chosen_one)

    def send_email(self, user, chosen_one):
        fromaddr = 'niven09@gmail.com'
        toaddrs  = user.email
        msg = 'Witaj {username}, wylosowales {chosen_one}. Kup cos fajnego!\n'.format(username=user.username, chosen_one=chosen_one.username)
        self.make_backup_message(msg)
        self.w_razie_w(user.username, msg)
        username = 'niven09@gmail.com'
        password = 'test'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

    def chose_chosen_one(self):
        random.shuffle(self.participants)
        chosen_one = self.participants[-1]
        lottery_match = []
        for participant in self.participants:
            match = [participant, chosen_one]
            lottery_match.append(match)
            chosen_one = participant
        return lottery_match

    def make_backup_message(self, text):
        with open('backup.txt','a+') as f:
            f.writelines(text)

    def w_razie_w(self,username, msg):
        with open(username + '_backup.txt','a+') as f:
            f.writelines(msg)