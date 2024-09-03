import sqlite3

class AnotacaoModel:
    def __init__(self):
        self.con = sqlite3.connect('database.db', check_same_thread=False)
        self.cursor = self.con.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS anotacoes")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS anotacoes(id_anotacao INTEGER PRIMARY KEY AUTOINCREMENT, conteudo TEXT NOT NULL, titulo TEXT NOT NULL, id_peca INTEGER NOT NULL, FOREIGN KEY(id_peca) REFERENCES peca(id_peca))")
        self.con.commit()

    def adicionar_nova_anotacao(self, id_peca, titulo, conteudo):
        self.cursor.execute("INSERT INTO anotacoes(titulo, conteudo, id_peca) values(?,?,?)",(titulo,conteudo, id_peca,))
        self.con.commit()
    def altera_anotacao(self, id_anotacao, titulo, conteudo):
        self.cursor.execute("UPDATE anotacoes SET titulo=?, conteudo=? WHERE id_anotacao=?",(titulo,conteudo, id_anotacao,))
        self.con.commit()
    
    #Retornos
    def retorna_anotacoes(self, id_peca:str):
        resultado = self.cursor.execute("SELECT * FROM anotacoes WHERE id_peca=?", (id_peca,))
        return resultado.fetchall()
    def retorna_anotacao(self, id_anotacao:str):
        resultado = self.cursor.execute("SELECT conteudo FROM anotacoes WHERE id_anotacao=?",(id_anotacao,))
        return resultado.fetchone()
