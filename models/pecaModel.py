import sqlite3
import os
class PecaModel:
    def __init__(self):
        self.con = sqlite3.connect('database.db', check_same_thread=False)
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pecas(id_peca INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, roteiro TEXT NOT NULL)")


    def criar_nova_peca(self, titulo:str, roteiro:str):
        self.cursor.execute("INSERT INTO pecas(titulo, roteiro) values(?,?)",(titulo, roteiro,))
        self.con.commit()

    def alterar_peca(self, id_peca:str, titulo:str, roteiro:str):
        self.cursor.execute("UPDATE pecas SET titulo=? WHERE id_peca=?",(titulo, id_peca,))
        self.cursor.execute("UPDATE pecas SET roteiro=? WHERE id_peca=?",(roteiro, id_peca,))
        self.con.commit()
    def deletar_peca(self, id_peca:str):
        self.cursor.execute("SELECT caminho from audios WHERE id_peca=?",(id_peca,))
        audios = self.cursor.fetchall()
        
        if audios:
            for audio in audios:
                os.remove(audio[0])
        self.cursor.execute("DELETE from pecas WHERE id_peca=?",(id_peca,))
        self.cursor.execute("DELETE from audios WHERE id_peca=?",(id_peca,))
        self.cursor.execute("DELETE from anotacoes WHERE id_peca=?",(id_peca,))
        
        self.con.commit()

    #Retornos
    def retorna_roteiro(self, id_peca:str):
        self.cursor.execute("SELECT roteiro from pecas WHERE id_peca=?",(id_peca,))
        return self.cursor.fetchall()
    
    def retorna_titulo_peca(self, id_peca:str):
        self.cursor.execute("SELECT titulo from pecas WHERE id_peca=?",(id_peca,))
        return self.cursor.fetchall()

    def retorna_pecas(self):
        self.cursor.execute("SELECT * from pecas")
        return self.cursor.fetchall()

    def retorna_peca(self, id_peca):
        self.cursor.execute("SELECT * from pecas WHERE id_peca=?", (id_peca,))
        return self.cursor.fetchone()