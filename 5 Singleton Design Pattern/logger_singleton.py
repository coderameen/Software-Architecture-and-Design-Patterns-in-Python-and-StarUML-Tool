class Logger:
    _instance = None#

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")

# Client Code
logger1 = Logger()
logger2 = Logger()

logger1.log("This is a log message.")
print(logger1 is logger2)  # Output: True