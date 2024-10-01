class RealResource:
    def access_resource(self):
        return "Accessing protected resource."

class Proxy:
    def __init__(self, user):
        self.user = user
        self.resource = RealResource()

    def access(self):
        if self.user == "admin":
            return self.resource.access_resource()
        return "Access denied."

# Client Code
proxy1 = Proxy("admin")
proxy2 = Proxy("guest")

print(proxy1.access())  # Allowed
print(proxy2.access())  # Denied
