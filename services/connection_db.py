import datetime
import sqlite3
import time

from utils import broadcast



class Oracle_db:

    broadcast = broadcast.Broadcast()


    def login(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("VERIFICANDO CREDENCIAIS")
        payload = self.broadcast.bdData()
        cursor.execute('SELECT * FROM usuario WHERE cpf = ? AND senha = ?', (tuple(payload)))

        user = cursor.fetchone()

        if user != None:

            if len(user) >=5:
                self.broadcast.credentials({"ID": user[0], "NAME": user[1], "CPF": user[2], "AGE": user[3]})
                self.broadcast.labelinfo("SUCESSO")
            else:
                self.broadcast.credentials("")
                self.broadcast.labelinfo("OCORREU UM ERRO")
        else:
            self.broadcast.credentials("")
            self.broadcast.labelinfo("CPF E/OU SENHA INCORRETOS")


        cursor.close()
        connection.close()

    def createUser(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("ENVIANDO DADOS PARA O BANCO")
        payload = self.broadcast.bdData()

        cursor.execute("INSERT INTO usuario (nome, cpf, nascimento, senha) VALUES (?, ?, ?, ?)",(tuple(payload)))


        if cursor.rowcount > 0:
            self.broadcast.labelinfo("USUÁRIO CADASTRADO COM SUCESSO!")

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        connection.commit()
        cursor.close()
        connection.close()


    def shopNewService(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("ENVIANDO DADOS PARA O BANCO")
        payload = self.broadcast.bdData()



        cursor.execute("INSERT INTO servico (cpf_colaborador, nome_servico, descricao, valor) VALUES (?, ?, ?, ?)",(tuple(payload)))


        if cursor.rowcount > 0:
            self.broadcast.labelinfo("SERVIÇO CADASTRADO COM SUCESSO!")
            connection.commit()

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")


        cursor.close()
        connection.close()



    def shopListService(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("BUSCANDO DADOS PARA O BANCO")
        payload = self.broadcast.bdData()

        cursor.execute("SELECT * FROM servico WHERE cpf_colaborador = ?", (payload[0],))

        user = cursor.fetchall()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("MOSTRANDO RESULTADOS")

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()



    def shopUpdateService(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("ATUALIZANDO O BANCO")
        payload = self.broadcast.bdData()

        cursor.execute( "UPDATE servico SET nome_servico = ?, descricao = ?, valor = ? WHERE id = ?", tuple(payload))

        user = cursor.fetchall()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("ITEM ATUALIZADO")
            connection.commit()

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()

    def shopDeleteService(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("ATUALIZANDO O BANCO")
        payload = self.broadcast.bdData()

        cursor.execute("DELETE FROM servico WHERE id = ?",(payload[0],))

        user = cursor.fetchall()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("ITEM DELETADO")
            connection.commit()

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()


    def clientListService(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("BUSCANDO DADOS NO BANCO")
        payload = self.broadcast.bdData()

        sql_query = "SELECT * FROM servico WHERE "
        params = []

        ctr = ""

        # Adicionar condição para o nome do serviço, se fornecido
        if payload[0] != "":
            sql_query += "nome_servico LIKE ?"
            params.append('%' + str(payload[0]).upper() + '%')

            if payload[1] != "":
                ctr = " AND "

        # Adicionar condição para o nome fantasia, se fornecido
        if payload[1] != "":
            sql_query += ctr + " cpf_colaborador IN (SELECT cpf FROM colaborador WHERE nome_fantasia LIKE ?) AND "
            params.append('%' + str(payload[1]).upper() + '%')

        # Remover o último "AND" da consulta
        sql_query = sql_query.rstrip("AND ")

        # Executar a consulta SQL
        cursor.execute(sql_query, tuple(params))

        user = cursor.fetchall()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("MOSTRANDO RESULTADOS")

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()

    def getShopInfo(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("BUSCANDO DADOS NO BANCO")
        payload = self.broadcast.bdData()

        cursor.execute("SELECT * FROM colaborador WHERE cpf = ?",(payload[0],))

        user = cursor.fetchone()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("MOSTRANDO RESULTADOS")

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()

    def shopListAllService(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("BUSCANDO DADOS PARA O BANCO")

        cursor.execute("SELECT * FROM servico")

        user = cursor.fetchall()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("MOSTRANDO RESULTADOS")

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()



    def getClientInfo(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("BUSCANDO DADOS NO BANCO")
        payload = self.broadcast.bdData()

        cursor.execute("SELECT * FROM cliente WHERE cpf = ?",(payload[0],))

        user = cursor.fetchone()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("MOSTRANDO RESULTADOS")

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()



    def clientInsertAddress(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("BUSCANDO DADOS PARA O BANCO")
        payload = self.broadcast.bdData()

        cursor.execute("SELECT * FROM cliente WHERE cpf = ?", (payload[0],))
        existing_cliente = cursor.fetchone()

        if existing_cliente:
            cursor.execute("UPDATE cliente SET endereco = ?, cep = ? WHERE cpf = ?",(payload[1], payload[2], payload[0]))

        else:
            cursor.execute("INSERT INTO cliente (cpf, endereco, cep) VALUES (?, ?, ?)",(payload[0], payload[1], payload[2]))

        user = cursor.fetchall()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("MOSTRANDO RESULTADOS")
            connection.commit()

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()





    def setShopInfo(self):



        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("BUSCANDO DADOS NO BANCO")
        payload = self.broadcast.bdData()

        # Verificar se já existe um colaborador associado ao mesmo CPF
        cursor.execute("SELECT * FROM colaborador WHERE cpf = ?", (payload[0],))
        existing_colaborador = cursor.fetchone()

        if existing_colaborador:
            # Atualizar os campos do colaborador existente
            cursor.execute("UPDATE colaborador SET nome_fantasia = ?, cnpj = ?, descricao = ? WHERE cpf = ?",tuple(payload))
            connection.commit()

        else:
            cursor.execute("INSERT INTO colaborador (cpf, nome_fantasia, cnpj, descricao) VALUES (?, ?, ?, ?)",tuple(payload))

        user = cursor.fetchone()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("MOSTRANDO RESULTADOS")
            connection.commit()

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()

    def getShopInfoByIdService(self):

            self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
            connection, cursor = self.__startConnection()

            self.broadcast.labelinfo("BUSCANDO DADOS NO BANCO")
            payload = self.broadcast.bdData()

            cursor.execute("""
                    SELECT c.*
                    FROM colaborador c
                    JOIN servico s ON c.cpf = s.cpf_colaborador
                    WHERE s.id = ?
                """, (payload[0],))

            user = cursor.fetchone()

            self.broadcast.dataTransfer(user)

            if cursor.rowcount > 0:
                self.broadcast.labelinfo("MOSTRANDO RESULTADOS")
                connection.commit()

            else:
                self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

            cursor.close()
            connection.close()

    def queueService(self):

        self.broadcast.labelinfo("CONECTANDO AO BANCO DE DADOS")
        connection, cursor = self.__startConnection()

        self.broadcast.labelinfo("BUSCANDO DADOS NO BANCO")
        payload = self.broadcast.bdData()

        # Verificar se a data do serviço é maior que a data atual
        data_atual = datetime.datetime.now().strftime('%dd-%MM-%yyyy')
        if payload[4] <= data_atual:
            print("Erro: A data do serviço deve ser maior que a data atual.")
            return

        # Adicionar o serviço à tabela
        cursor.execute('''
            INSERT INTO solicitacao_servico ( id_servico, cpf_cliente, nome_servico, valor, data_servico, observacao)
            VALUES ( ?, ?, ?, ?, ?, ?)
        ''',tuple(payload))

        user = cursor.fetchone()

        self.broadcast.dataTransfer(user)

        if cursor.rowcount > 0:
            self.broadcast.labelinfo("MOSTRANDO RESULTADOS")
            connection.commit()

        else:
            self.broadcast.labelinfo("NÃO FOI POSSÍVEL GRAVAR OS DADOS")

        cursor.close()
        connection.close()







    def __startConnection(self):


        # Connect to or create an SQLite database file
        connection = sqlite3.connect('./database/database.db')

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Create a table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            nascimento DATE NOT NULL,
            senha TEXT NOT NULL
        )    
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY,
                cpf TEXT NOT NULL,
                endereco TEXT NOT NULL,
                cep TEXT NOT NULL,
                FOREIGN KEY (cpf) REFERENCES usuario(cpf)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS colaborador (
                id INTEGER PRIMARY KEY,
                cpf TEXT NOT NULL,
                nome_fantasia TEXT NOT NULL,
                cnpj TEXT NOT NULL UNIQUE,
                descricao TEXT,
                FOREIGN KEY (cpf) REFERENCES usuario(cpf)
            )
        ''')

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS servico (
                    id INTEGER PRIMARY KEY,
                    cpf_colaborador TEXT NOT NULL,
                    nome_servico TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    valor TEXT NOT NULL,
                    FOREIGN KEY (cpf_colaborador) REFERENCES colaborador(cpf)
                )
            ''')

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS solicitacao_servico (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_servico INTEGER NOT NULL,
                    cpf_cliente TEXT NOT NULL,
                    nome_servico TEXT NOT NULL,
                    valor REAL NOT NULL,
                    data_servico DATE NOT NULL,
                    observacao TEXT,
                    FOREIGN KEY (cpf_cliente) REFERENCES cliente(cpf)
                )
            ''')


        return connection, cursor





