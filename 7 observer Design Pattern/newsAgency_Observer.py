# Subject (News Agency)
class NewsAgency:
    def __init__(self):
        self.subscribers = []
        self.news = ""

    # Subscribe a subscriber to the agency
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    # Notify all subscribers about the new news
    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self.news)

    # Set the news and notify all subscribers
    def set_news(self, news):
        self.news = news
        self.notify()

# Observer (Subscriber)
class Subscriber:
    def update(self, news):
        print(f"News received: {news}")

# Client Code
if __name__ == "__main__":
    # Create the news agency (Subject)
    agency = NewsAgency()

    # Create subscriber instances (Observers)
    sub1 = Subscriber()
    sub2 = Subscriber()

    # Subscribe the subscribers to the news agency
    agency.subscribe(sub1)
    agency.subscribe(sub2)

    # Set the news and notify all subscribers
    agency.set_news("Breaking News: Observer Pattern in Python!")
