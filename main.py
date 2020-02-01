import firebaseConfig as FC
from soldier import soldier

firebase = FC.firebaseMain

db = firebase.database()
users = db.child("soldier_data").get()



# method to extract all soldier entry in database 
def all_soldier_id():
    for user in users.each():
        print(user.key())



# method to extract soldier data using his name
def search_soldier(args):
    user = db.child("soldier_data").child(args).get()
    if user.val() is None:
        print("No such Solider Found")
    else:
        print(user.val())


#data = {"name": "Vishesh"}
#db.child("soldier_data").child("Soldier Id").set(data)

all_soldier_id()
search_soldier("Rameshh")
