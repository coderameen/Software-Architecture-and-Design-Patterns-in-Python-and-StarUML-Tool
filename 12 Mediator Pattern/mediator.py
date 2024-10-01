class ChatRoom:
    def __init__(self):
        self.participants = []
        
    def add(self, participant):
        self.participants.append(participant)
        participant.room = self#create a room
        
    def send(self,sender,message):
        for p in self.participants:
            if p != sender:
                p.receive(message, sender.name)
                
class Participant:
    def __init__(self, name):
        self.name = name
    def send(self,msg):
        # Use the room's send method to send the message
        self.room.send(self, msg)
    def receive(self, msg, sender):
         # Print the message from sender
        print(f"{sender}: {msg}")

# Client Code
room = ChatRoom()
alice = Participant("Alice")
bob = Participant("Bob")

room.add(alice)
room.add(bob)

alice.send("Hi Bob!")
bob.send("Hi Amen")