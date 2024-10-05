class ChatRoom:
    def __init__(self):
        self.participants = []

    def add(self, p):
        self.participants.append(p)
        p.room = self

    def send(self, sender, msg):
        for p in self.participants:
            if p != sender:
                p.receive(msg, sender.name)

class Participant:
    def __init__(self, name):
        self.name = name

    def send(self, msg):
        self.room.send(self, msg)

    def receive(self, msg, sender):
        print(f"{sender}: {msg}")

# Example
room = ChatRoom()
alice, bob = Participant("Alice"), Participant("Bob")
room.add(alice)
room.add(bob)
alice.send("Hi Bob!")
