import sqlite3
import scipy.io.wavfile as wav
class AudioModel:
    def __init__(self):
        self.con = sqlite3.connect('database.db', check_same_thread=False)
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS audios(id_audio INTEGER PRIMARY KEY AUTOINCREMENT, caminho TEXT NOT NULL, texto TEXT NOT NULL, id_peca INTEGER NOT NULL, FOREIGN KEY (id_peca) REFERENCES pecas(id_peca))")
        self.con.commit()
    
    def criar_novo_audio(self, texto:str, id_peca:str, audio):
        self.cursor.execute("SELECT max(id_audio) from audios")
        atual = self.cursor.fetchone()
        if atual[0]:
            print("ATUal")
            print(atual)
            caminho=f"audios/{atual[0]+1}.wav"
        else:
            caminho=f"audios/1.wav"
        wav.write(caminho, 44100, audio)
        self.cursor.execute("INSERT INTO audios(texto, caminho, id_peca) values(?,?,?)",(texto, caminho, id_peca,))
        self.con.commit()
    
    def retorna_audios(self, id_peca:str):
        self.cursor.execute("SELECT * FROM audios WHERE id_peca=?",(id_peca,))
        return self.cursor.fetchall()