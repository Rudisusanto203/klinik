from app.extensions._db import db


class Pemberian_ObatModel(db.Model):
    __tablename__ = 'pemberian_obat'

    keterangan_rawat = db.Column(db.String(128), primary_key=True)
    no_opname = db.Column(db.Integer, nullable=True)
    no_rm = db.Column(db.Integer, nullable=True)
    nama_pasien = db.Column(db.String(128), nullable=False)
    keterangan = db.Column(db.String(128), nullable=False)
    tgl_tindakan = db.Column(db.String(128), nullable=False)
    data_obat = db.Column(db.String(128), nullable=False)
    kode_obat = db.Column(db.String(128), nullable=False)
    dosis_obat = db.Column(db.String(128), nullable=False)





    def __repr(self):
        return f"<Pemberian_Obat {self.no_opname}>"
