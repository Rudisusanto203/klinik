from app.extensions._db import db


class Laporan_Rekam_MedisModel(db.Model):
    __tablename__ = 'laporan_rekam_medis'
    
    laporan_rekam_medis = db.Column(db.String(128), primary_key=True)
   

    def __repr(self):
        return f"<Laporan_Rekam_Medis {self.nama_username}>"
