import firebaseConfig as FC

firebase = FC.firebaseMain




db = firebase.database()
print(db)


data = {"name": "Vishesh"
        }

db.child("soldier_data").child("Soldier Id").set(data)

users = db.child("soldier_data").get()
for user in users.each():
    print(user.key()) # Morty
    print(user.val()) # {name": "Mortimer 'Morty' Smith"}