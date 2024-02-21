class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


information = input()
emails = []

while information != "Stop":

    information = information.split()
    sender = information[0]
    receiver = information[1]
    content = information[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    information = input()

indexes = [int(index) for index in input().split(", ")]

for index in indexes:
    emails[index].send()

