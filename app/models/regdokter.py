from app.extensions._db import db


class RegDokterModel(db.Model):
    __tablename__ = 'regdokter'

    id_dokter = db.Column(db.Integer, primary_key=True)
    nama_dokter = db.Column(db.String(128), nullable=False)
    no_hp = db.Column(db.Integer, primary_key=True)
    alamat = db.Column(db.String(128), nullable=False)
    spesialis = db.Column(db.String(128), nullable=False)


    def __repr(self):
        return f"<RegPasien {self.nama_dokter}>"
