#Tutorial 4 Dictionaries
#1 Create a Dictionary that stores pet information
#2 Change values within the dictionary
#3 Add values to the dictionary

pet1 = {
'name' : 'Bonnie',
'animal_category' :'Cat',
'age' : 3,
'vaccinated' : True
'credt_card' : '3423 2326 7543 1234'
'billing_address' : '17 Park Drive, The Shire 3695',
'owner_name' : 'Annie Jenkins',
'account_balance' : 129.95,
}

pet1['vaccinated'] = False

for item in pet1:
    print(item,':', pet1[item])
 
#ACTIVITIES:
#1. Change name to Miss Bonnie
#2. Increase age by 1
#3. Create another pet who is a dog, fill in all the fields
