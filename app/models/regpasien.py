from app.extensions._db import db


class RegPasienModel(db.Model):
    __tablename__ = 'regpasien'

    id_ktp = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(128), nullable=False)
    ttgl = db.Column(db.String(128), unique=True, nullable=False)
    jenis_kelamin = db.Column(db.String(128), nullable=False)
    status_perkawinan= db.Column(db.String(128), nullable=False)
    agama = db.Column(db.String(128), nullable=False)
    alamat = db.Column(db.String(128), nullable=False)
    pekerjaan = db.Column(db.String(128), nullable=False)
    no_hp = db.Column(db.Integer, primary_key=True)
    kategori_pasien = db.Column(db.String(128), nullable=False)
    jenis_kelamin = db.Column(db.String(128), nullable=False)
    

    def __repr(self):
        return f"<RegPasien {self.nama_lengkap}>"
