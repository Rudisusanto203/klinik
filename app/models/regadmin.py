from app.extensions._db import db


class RegAdminModel(db.Model):
    __tablename__ = 'regadmin'
    
    nama = db.Column(db.String(128), primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    alamat = db.Column(db.String(128), nullable=False)


    def __repr(self):
        return f"<RegAdmin {self.nama_username}>"
