class Employee:
    raise_amt = 1.05

    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary

    # property decortaor
    @property
    def emailemployee(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


#local testing 
e = Employee("peter")
print(e.emaileemployee)
print(f"current salary = {e.salary}")
e.apply_raise()
print(f"after raising the salary = {e.salary}") # after raises