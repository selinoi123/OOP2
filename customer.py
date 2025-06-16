
class Customer:

    def __init__(self, name, email, _id):
        self.name = name
        self.email = email
        self._id = _id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if isinstance(value, int) and value > 0:
            self._id = value
        else:
            raise ValueError("ID must be a positive integer")

    def __str__(self):
        return f"Customer {self.name} (ID : {self._id})  - Email : {self.email}"

    def __repr__(self):
        return f"Customer (name={repr(self.name)}, email={self.email}, id={self._id})"



c1 = Customer("Alice", "alice@example.com", 101)
c2 = Customer("Bob", "bob@example.com", 202)

print(c1)
print(repr(c2))

