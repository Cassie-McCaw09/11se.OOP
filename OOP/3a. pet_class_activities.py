# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class Pet:
    def __init__(self, name, category, age,):
        self.name = name
        self.category = category 
        self.age = age
        self.vaccinated = False

p1 = Pet('Bonnie', 'Cat', 3)
p2 = Pet('Foxy', 'Dog', 5)

print(p2.name)
print(p2.category)
print(p2.vaccinated)



name = "Bonnie",
animal_category =  "Cat",
age = 3,
vaccinated  = True,
credit_card = "3423 2326 7543 1234",
billing_address = "17 Park Drive, The Shire 3695",
owner_name = "Annie Jenkins",
account_balance = 129.95,



#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)