# Import database module.
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference('bestcamera-7e901.firebaseio.com/test')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())
