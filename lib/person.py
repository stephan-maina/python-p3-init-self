class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.friends = []

    def greet(self):
        return f"Hello, my name is {self.name}."

    def introduce(self):
        return f"I am {self.name}, {self.age} years old, and I am {self.gender}."

    def add_friend(self, friend):
        self.friends.append(friend)
        return f"{self.name} is now friends with {friend.name}."

    def list_friends(self):
        if self.friends:
            return f"{self.name}'s friends: {', '.join([friend.name for friend in self.friends])}"
        else:
            return f"{self.name} has no friends yet."

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nFriends: {', '.join([friend.name for friend in self.friends])}"

if __name__ == "__main__":
    Samuel = Person("Samuel", 28, "male")
    Muserian = Person("Muserian", 30, "female")
    Winnie = Person("Winnie", 25, "female")
    Noel = Person("Noel", 35, "male")

    print(samuel.greet())
    print(muserian.introduce())

    print(samuel.add_friend(winnie))
    print(muserian.add_friend(noel))

    print(samuel.list_friends())
    print(muserian.list_friends())

    print("Samuel's Info:")
    print(samuel)

    print("Muserian's Info:")
    print(muserian)
