class Human:
    def __init__(self, name, birthday, age, country, city, number, address):
        self.fullName = name
        self.birthDay = birthday
        self.age = age
        self.country = country
        self.city = city
        self.phoneNumber = number
        self.homeAddress = address

    def showInfo(self):
        print(f"fullName:{self.fullName}")
        print(f"birthDay:{self.birthDay}")
        print(f"country:{self.country}")
        print(f"city:{self.city}")
        print(f"phoneNumber:{self.phoneNumber}")
        print(f"homeAddress:{self.homeAddress}")

    def setAge(self, birthday):
        self.age = birthday

    def getAge(self):
        return self.age

person = Human(name="Alexandra Pushkina", birthday="25-01-2005", age=19, country="Ukraine", city="Kryvyi Rih", number="380935555551", address="Dnepropetrovskoye chasse")
person.setAge(20)
print(person.getAge())
person.showInfo()