from app.extensions._db import db


class Data_Rekam_MedisModel(db.Model):
    __tablename__ = 'regpasien'

    no_reg = db.Column(db.Integer, primary_key=True)
    no_rm = db.Column(db.Integer, nullable=False)
    id_ktp = db.Column(db.Integer, nullable=False)
    nama_lengkap = db.Column(db.String(128), nullable=False)
    ttgl = db.Column(db.String(128), unique=True, nullable=False)
    jenis_kelamin = db.Column(db.String(128), nullable=False)
    status_perkawinan= db.Column(db.String(128), nullable=False)
    agama = db.Column(db.String(128), nullable=False)
    alamat = db.Column(db.String(128), nullable=False)
    pekerjaan = db.Column(db.String(128), nullable=False)
    keluarga_terdekat = db.Column(db.String(128), nullable=False)
    tanggal_masuk = db.Column(db.String(128), nullable=False)
    tanggal_keluar = db.Column(db.String(128), nullable=False)
    ruangan = db.Column(db.String(128), nullable=False)
    keluhan = db.Column(db.String(128), nullable=False)
    riwayat_peyakit_dahulu = db.Column(db.String(128), nullable=False)
    riwayat_alergi_obat = db.Column(db.String(128), nullable=False)
    diagnosa = db.Column(db.String(128), nullable=False)


    def __repr(self):
        return f"<Data_Rekam_Medis {self.no_rm}>"
