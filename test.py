from database import db
from database import app
db.create_all()
from database import id
admin1 = id(id_picture="1")
print(admin1)
db.session.add(admin1)
db.session.commit()
