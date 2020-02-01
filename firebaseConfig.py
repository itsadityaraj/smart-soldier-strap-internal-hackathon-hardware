import pyrebase

config = {
  "apiKey": "AIzaSyCCt4ts2uP_Z3V8TQOkMaTPIUSHaiYa-ko",
  "authDomain": "kautilya-academy-d4162.firebaseapp.com",
  "databaseURL": "https://kautilya-academy-d4162.firebaseio.com",
  "storageBucket": "kautilya-academy-d4162.appspot.com",
  "serviceAccount": "kautilya-academy-d4162-857f562fdd13.json"
}
firebaseMain = pyrebase.initialize_app(config)
