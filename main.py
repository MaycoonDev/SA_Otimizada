from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import sqlite3

app = Tk()

class funcs():
    def conecta(self):
        self.conn = sqlite3.connect('tiffanytech.sql')
        self.cursor = self.conn.cursor()
        print('Conectado ao Banco de dados')

    def desconecta(self):
        self.conn.close()
        print('Desconectado do Banco de Dados')

    def criatabelas(self):
        self.conecta()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
                               id integer PRIMARY KEY AUTOINCREMENT,
                               nome VARCHAR(100) NOT NULL,
                               cpf integer(15) NOT NULL,
                               telefone integer(15) NOT NULL
                               );""")
        self.conn.commit()
        self.desconecta()
        self.conecta()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS agendamento (
                               id integer PRIMARY KEY AUTOINCREMENT,
                               nome VARCHAR(100) NOT NULL,
                               servico VARCHAR(100) NOT NULL,
                               atendente VARCHAR(100) NOT NULL,
                               valor FLOAT(15) NOT NULL,
                               horario DATETIME NOT NULL,
                               situacao VARCHAR(100) NOT NULL
                               );""")

        self.conn.commit();
        print('Tabelas criada')
        self.desconecta()

    def limparcampos1(self):
        self.inpnome.delete(0, END)
        self.inpatn.delete(0, END)
        self.inpserv.delete(0, END)
        self.inpvlr.delete(0, END)
        self.inpdata.delete(0, END)
        self.inpsitu.delete(0, END)
        self.inpid.delete(0, END)

    def limparcampos2(self):
        self.inpnome.delete(0, END)
        self.inpcpf.delete(0, END)
        self.inptel.delete(0, END)
        self.inpid.delete(0, END)

    def limparcampos3(self):
        self.lbnomev['text'] =''
        self.lbatnv['text'] =''
        self.lbserv['text'] =''
        self.lbvlrv['text'] =''
        self.lbdatav['text'] =''
        self.lbsituv['text'] =''

        self.inpid.delete(0, END)
        self.inpnomen.delete(0, END)
        self.inpatnn.delete(0, END)
        self.inpservn.delete(0, END)
        self.inpvlrn.delete(0, END)
        self.inpdatan.delete(0, END)
        self.inpsitun.delete(0, END)

    def limparcampo4(self):
        self.lbnome['text'] = ''
        self.lbcpf['text'] = ''
        self.lbtel['text'] = ''
        self.inpnomen.delete(0, END)
        self.inpcpfn.delete(0, END)
        self.inpteln.delete(0, END)

    def limparcampos5(self):
        self.lbnome['text'] = ''
        self.lbcpf['text'] = ''
        self.lbtel['text'] = ''
        self.inpid.delete(0, END)

    def limparcampos6(self):
        self.lbnomev['text'] = ''
        self.lbatnv['text'] = ''
        self.lbserv['text'] = ''
        self.lbvlrv['text'] = ''
        self.lbdatav['text'] = ''
        self.lbsituv['text'] = ''

    def agendamento(self):
        self.conecta()
        self.nome = self.inpnome.get()
        self.atendente = self.inpatn.get()
        self.servico = self.inpserv.get()
        self.valor = self.inpvlr.get()
        self.data = self.inpdata.get()
        self.situacao = self.inpsitu.get()
        if self.nome == '' or self.atendente == '' or self.servico == '' or self.valor == '' or self.data == '' or self.data == '' or self.situacao == '':
            MessageBox.showinfo('Confira os campos', 'Algum campo esta em falta')
        else:
            print(f'Nome do Cliente: {self.nome}\nNome do Atendente: {self.atendente}\nTipo de Serviço: {self.servico}\nValor: {self.valor}\nData: {self.data}\nSituação: {self.situacao}')
            self.cursor.execute('INSERT INTO agendamento (nome,servico,atendente,valor,horario,situacao) VALUES (?,?,?,?,?,?)',(self.nome, self.servico, self.atendente, self.valor, self.data, self.situacao))
            self.conn.commit()
            MessageBox.showinfo('Status de Agendamento', 'Horario Marcado com Sucesso')
            self.limparcampos1()
        self.listaagn()
        self.desconecta()

    def buscaidagn(self):
        self.conecta()
        self.id = self.inpid.get()
        self.cursor.execute('SELECT * FROM agendamento WHERE id = (?)', (self.id,))

        for i in self.cursor.fetchall():
            self.lbnomev['text'] = i[1]
            self.lbserv['text'] = i[2]
            self.lbatnv['text'] = i[3]
            self.lbvlrv['text'] = i[4]
            self.lbdatav['text'] = i[5]
            self.lbsituv['text'] = i[6]
            self.conn.commit()
        self.desconecta()

    def atagendamento(self):
        self.buscaidagn()
        self.conecta()
        self.id = self.inpid.get()
        self.nome = self.inpnomen.get()
        self.servico = self.inpservn.get()
        self.atendente = self.inpatnn.get()
        self.valor = self.inpvlrn.get()
        self.data = self.inpdatan.get()
        self.situacao = self.inpsitun.get()

        if not self.nome:
            self.nome = self.lbnomev['text']
        if not self.servico:
            self.servico = self.lbserv['text']
        if not self.atendente:
            self.atendente = self.lbatnv['text']
        if not self.valor:
            self.valor = self.lbvlrv['text']
        if not self.data:
            self.data = self.lbdatav['text']
        if not self.situacao:
            self.situacao = self.lbsituv['text']

        self.cursor.execute('UPDATE agendamento SET nome = ?, servico = ?, atendente = ?, valor = ?, horario = ?, situacao = ? WHERE id = ?', (self.nome,self.servico,self.atendente,self.valor,self.data,self.situacao,self.id))
        self.conn.commit()
        MessageBox.showinfo('Concluido', 'Os Dados do Cliente Foram Atualizados')
        self.limparcampos3()
        self.desconecta()

    def deletaragn(self):
        self.buscaidagn()
        self.conecta()
        self.id = self.inpid.get()
        self.cursor.execute('DELETE FROM agendamento WHERE id = ?', (self.id,))
        self.conn.commit()
        MessageBox.showinfo('Concluido', 'Cliente Deletado Com Sucesso')
        self.limparcampos6()
        self.desconecta()

    def cadcli(self):
        self.conecta()
        self.nome = self.inpnome.get()
        self.cpf = self.inpcpf.get()
        self.telefone = self.inptel.get()
        if self.nome == '' or self.cpf == '' or self.telefone == '':
            MessageBox.showinfo('Confira os campos', 'Algum campo esta em falta')
        else:
            print(f'Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}')
            self.cursor.execute('insert into clientes (nome,cpf,telefone) values(?,?,?)',(self.nome, self.cpf, self.telefone))
            self.conn.commit()
            MessageBox.showinfo('Dados inseridos', 'Cliente cadastrado com sucesso')
            self.desconecta()
            self.limparcampos2()
            self.listacli()

    def buscacli(self):
        self.conecta()
        self.id = self.inpid.get()
        self.cursor.execute('SELECT * FROM clientes WHERE id = (?)', (self.id,))

        for a in self.cursor.fetchall():
            self.lbnome['text'] = a[1]
            self.lbcpf['text'] = a[2]
            self.lbtel['text'] = a[3]
            self.conn.commit()
        self.desconecta()

    def atcliente(self):
        self.buscacli()
        self.conecta()

        self.id = self.inpid.get()
        self.nome = self.inpnomen.get()
        self.cpf = self.inpcpfn.get()
        self.telefone = self.inpteln.get()

        if not self.nome:
            self.nome = self.lbnome['text']
        if not self.cpf:
            self.cpf = self.lbcpf['text']
        if not self.telefone:
            self.telefone = self.lbtel['text']

        self.cursor.execute('UPDATE clientes SET nome = ? , cpf = ? , telefone = ? WHERE id = ?', (self.nome, self.cpf, self.telefone, self.id))
        self.conn.commit()
        MessageBox.showinfo('Concluido', 'Os Dados do Cliente Foram Atualizados')
        self.limparcampo4()
        self.desconecta()

    def deletarcli(self):
        self.buscacli()
        self.conecta()
        self.id = self.inpid.get()
        self.cursor.execute('DELETE FROM clientes WHERE id = ?', (self.id,))
        self.conn.commit()
        MessageBox.showinfo('Concluido', 'Cliente Deletado Com Sucesso')
        self.limparcampos5()
        self.desconecta()

    def listaagn(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conecta()
        lista = self.cursor.execute('SELECT * FROM agendamento ORDER BY id ')
        for a in lista:
            self.tabela.insert('', END, values=a)
        self.desconecta()

    def listacli(self):
        self.tabelacli.delete(*self.tabelacli.get_children())
        self.conecta()
        lista = self.cursor.execute('SELECT * FROM clientes ORDER BY id ')
        for a in lista:
            self.tabelacli.insert('', END, values=a)
        self.desconecta()

    def filtroagn(self):
        self.id = self.inpid.get()
        self.tabela.delete(*self.tabela.get_children())
        self.conecta()
        lista = self.cursor.execute('SELECT * FROM agendamento WHERE id = ? ', (self.id,))
        for a in lista:
            self.tabela.insert('', END, values=a)
        self.desconecta()

    def filtrocli(self):
        self.id = self.inpid.get()
        self.tabelacli.delete(*self.tabelacli.get_children())
        self.conecta()
        lista = self.cursor.execute('SELECT * FROM clientes WHERE id = ? ',(self.id,))
        for a in lista:
            self.tabelacli.insert('', END, values=a)
        self.desconecta()

class aplicativo(funcs):
    def __init__(self):
        self.app = app
        self.criatabelas()
        self.telamain()
        self.frames()
        self.tabelaagn()
        self.labels()
        self.inputs()
        self.botoes()
        self.listaagn()
        self.app.mainloop()

    def telamain(self):
        self.app.title('Salão Tiffany')
        self.app.geometry('700x500')
        self.app.resizable(False, False)
        self.app.configure(background='#CD5C5C')
        self.app.iconbitmap('mdchefeicon.ico')

    def frames(self):
        self.bdcima= Label(self.app, background='#000')
        self.bdcima.place(relx=0.004, rely=0.01, relwidth=0.98, relheight=0.48)
        self.bdbaixo = Label(self.app, background='#000')
        self.bdbaixo.place(relx=0.004, rely=0.50, relwidth=0.98, relheight=0.48)

        #FRAME DE CIMA
        self.frame1 = Frame(self.app, background='#FFC0CB')
        self.frame1.place(x=7,y=7,width=680,height=235)

        #BORDA DO FRAME3
        self.bdmeio = Label(self.frame1, background='#000')
        self.bdmeio.place(x=398, y=23, width=229, height=179)

        # linhas dentro do frame1
        self.linhadecima = Label(self.frame1, background='#000')
        self.linhadecima.place(x=10, y=10, relwidth=0.97, height=2)
        self.linhadebaixo = Label(self.frame1, background='#000')
        self.linhadebaixo.place(x=10, y=220, relwidth=0.97, height=2)

        #FRAME DE BAIXO
        self.frame2 = Frame(self.app, background='#FFC0CB')
        self.frame2.place(relx=0.01,rely=0.51,relwidth=0.97,relheight=0.46)

        #FRAME DENTRO DO FRAME1
        self.frame3 = Frame(self.frame1, background='#CD5C5C')
        self.frame3.place(x=400,y=25,width=225,height=175)

        #linha dentro do frame3
        self.linhameio = Label(self.frame3, background='#000')
        self.linhameio.place(x=8,y=75,width=210,height=2)

        #segunda linha do frame3
        self.linhameio2 = Label(self.frame3, background='#000')
        self.linhameio2.place(x=8, y=120, width=210, height=2)

    def tabelaagn(self):
        self.tabela = ttk.Treeview(self.frame2, height=30, column=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7','col8'))
        self.tabela.heading('#0', text='')
        self.tabela.heading('#1', text='ID')
        self.tabela.heading('#2', text='Nome do Cliente')
        self.tabela.heading('#3', text='Serviço')
        self.tabela.heading('#4', text='Atendente')
        self.tabela.heading('#5', text='Valor')
        self.tabela.heading('#6', text='Data')
        self.tabela.heading('#7', text='Situação')


        self.tabela.column('#0', width=1)
        self.tabela.column('#1', width=30)
        self.tabela.column('#2', width=100)
        self.tabela.column('#3', width=100)
        self.tabela.column('#4', width=100)
        self.tabela.column('#5', width=90)
        self.tabela.column('#6', width=70)
        self.tabela.column('#7', width=100)

        self.tabela.place(x=10, y=10, width=628, height=210)

        self.barrarolagem = Scrollbar(self.frame2, orient='vertical')
        self.tabela.configure(yscroll=self.barrarolagem.set)
        self.barrarolagem.place(x=638, y=40, width=31, height=180)

    def labels(self):
        # nome
        self.lbnome = Label(self.frame1, text='Nome do Cliente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbnome.place(x=10, y=20, width=94, height=15)

        # serviço
        self.lbserv = Label(self.frame1, text='Serviço', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbserv.place(x=10,y=55,width=40,height=15)

        # atendente
        self.lbatn = Label(self.frame1, text='Nome do Atendente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbatn.place(x=10, y=90, width=114, height=15)

        # valor
        self.lbvlr = Label(self.frame1,text='Valor R$', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbvlr.place(x=10,y=125,width=45,height=15)

        # data
        self.lbdata = Label(self.frame1,text='Data dd/mm/aa hh:mm', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbdata.place(x=10,y=160,width=130,height=15)

        # situação
        self.lbsitu = Label(self.frame1,text='Situação', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbsitu.place(x=10,y=195,width=45,height=15)

        #id
        self.lbid = Label(self.frame3,text='Id', font=('calibri', 13, 'bold'), background='#CD5C5C',foreground='#000')
        self.lbid.place(x=30,y=135,width=15,height=20)

    def inputs(self):
        # nome
        self.inpnome = Entry(self.frame1,background='#ffffff',foreground='#000',font=('calibri',10))
        self.inpnome.place(x=109, y=20, width=200, height=15)

        #serviço
        self.inpserv = Entry(self.frame1,background='#ffffff',foreground='#000',font=('calibri',10))
        self.inpserv.place(x=55,y=55,width=100,height=15)

        # atendente
        self.inpatn = Entry(self.frame1, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpatn.place(x=129, y=90, width=200, height=15)

        #valor
        self.inpvlr = Entry(self.frame1,background='#ffffff',foreground='#000',font=('calibri',10))
        self.inpvlr.place(x=60,y=125,width=50,height=15)

        #data
        self.inpdata = Entry(self.frame1, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpdata.place(x=145,y=160,width=120,height=15)

        #situação
        self.inpsitu = Entry(self.frame1, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpsitu.place(x=60,y=195,width=70,height=15)

        #id
        self.inpid = Entry(self.frame3,background='#ffffff',foreground='#000', font=('calibri', 10))
        self.inpid.place(x=50,y=135,width= 50, height=20)

    def botoes(self):
        #botao marca hora
        self.btmarca = Button(self.frame3,text='Marcar Horario',font=('calibri',10,'bold'),background='#FFC0CB',foreground='#000',command=self.agendamento)
        self.btmarca.place(x=10,y=10,width=100,height=25)

        #botao atualizar
        self.btatualizar = Button(self.frame3,text='Atualizar',font=('calibri',10,'bold'),background='#FFC0CB',foreground='#000',command=atualizaragn)
        self.btatualizar.place(x=115,y=10,width=100,height=25)

        #botao limpar campos
        self.btlimpar = Button(self.frame3,text='Limpar Campos',font=('calibri',10,'bold'),background='#FFC0CB',foreground='#000',command=self.limparcampos1)
        self.btlimpar.place(x=10,y=40,width=100,height=25)

        #botao de deletar
        self.btdelete = Button(self.frame3,text='Deletar Agn.',font=('calibri',10,'bold'),background='#FFC0CB',foreground='#000',command=deletaragn)
        self.btdelete.place(x=115,y=40,width=100,height=25)

        #botao tabela de clientes
        self.btcliente = Button(self.frame3,text='Clientes',font=('calibri',10,'bold'),background='#FFC0CB',foreground='#000',command=cliente)
        self.btcliente.place(x=10,y=85,width=205,height=25)

        #BOTAO FILTRO
        self.btfiltro = Button(self.frame3,text='Filtrar',font=('calibri',10,'bold'),background='#FFC0CB',foreground='#000',command=self.filtroagn)
        self.btfiltro.place(x=105,y=133,width=100,height=25)

        #botao recarregar
        self.photo = PhotoImage(file=r"C:\Users\mayco\Desktop\meu_projeto\refresh.png")
        self.photo1 = self.photo.subsample(13,13)
        self.brrefresh = Button(self.frame2,image=self.photo1,background='#FFC0CB',foreground='#000',command=self.listaagn)
        self.brrefresh.place(x=636,y=10,width=33,height=33)

class atualizaragn(funcs):
    def __del__(self):
        self.telaatagn()
        self.frames()
        self.labelsatagn()
        self.inpuatagn()
        self.botaoatagn()

    def telaatagn(self):
        self.app5 = Toplevel()
        self.app5.title('Atualizar Agendamento')
        self.app5.geometry('590x220')
        self.app5.resizable(False, False)
        self.app5.iconbitmap(r'mdchefeicon.ico')
        self.app5.configure(background='#CD5C5C')
        self.app5.transient(app)
        self.app5.focus_force()
        self.app5.grab_set()

    def frames(self):
        # bordas
        self.bdcima = Label(self.app5, background='#000')
        self.bdcima.place(x=5, y=5, width=574, height=205)
        # frame de cima da tela clientes
        self.frame9 = Frame(self.app5, background='#FFC0CB')
        self.frame9.place(x=7, y=7, width=570, height=200)
        # linha d cima
        self.linhacima = Label(self.frame9, background='#000')
        self.linhacima.place(x=5, y=30, width=557, height=2)

    def labelsatagn(self):
        # id
        self.lbid = Label(self.frame9, text='Id', font=('calibri', 10, 'bold'), background='#FFC0CB', foreground='#000')
        self.lbid.place(x=7, y=7, width=15, height=15)

        # dados atuais
        self.atual = Label(self.frame9, text='Dados Atuais', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.atual.place(x=100, y=40, width=75, height=15)

        # nome
        self.lbnome = Label(self.frame9, text='Nome do Cliente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbnome.place(x=7, y=60, width=94, height=15)

        # serviço
        self.lbserv = Label(self.frame9, text='Serviço', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbserv.place(x=7, y=80, width=40, height=15)

        # atendente
        self.lbatn = Label(self.frame9, text='Nome do Atendente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbatn.place(x=7, y=100, width=114, height=15)

        # valor
        self.lbvlr = Label(self.frame9, text='Valor R$', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbvlr.place(x=7, y=120, width=45, height=15)

        # data
        self.lbdata = Label(self.frame9, text='Data dd/mm/aa hh:mm', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbdata.place(x=7, y=140, width=130, height=15)

        # situação
        self.lbsitu = Label(self.frame9, text='Situação', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbsitu.place(x=7, y=160, width=45, height=15)
        #--------------------------------------------------------------------------------------------------------------#
        # nome velho
        self.lbnomev = Label(self.frame9, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbnomev.place(x=142, y=60, width=200, height=15)

        # serviço velho
        self.lbserv = Label(self.frame9, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbserv.place(x=142, y=80, width=100, height=15)

        # atendente velho
        self.lbatnv = Label(self.frame9, text='', font=('calibri', 10, 'bold'), background='#ffffff', foreground='#000')
        self.lbatnv.place(x=142, y=100, width=200, height=15)

        # valor velho
        self.lbvlrv = Label(self.frame9, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbvlrv.place(x=142, y=120, width=50, height=15)

        # data velha
        self.lbdatav = Label(self.frame9, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbdatav.place(x=142, y=140, width=160, height=15)

        # situação velha
        self.lbsituv = Label(self.frame9, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbsituv.place(x=142, y=160, width=195, height=15)

        # dados novos
        self.novo = Label(self.frame9, text='Dados Novos', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.novo.place(x=382, y=40, width=75, height=15)

    def inpuatagn(self):
        # id busca
        self.inpid = Entry(self.frame9, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpid.place(x=27, y=7, width=50, height=15)

        # nome
        self.inpnomen = Entry(self.frame9, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpnomen.place(x=347, y=60, width=200, height=15)

        # serviço
        self.inpservn = Entry(self.frame9, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpservn.place(x=347, y=80, width=100, height=15)

        # atendente
        self.inpatnn = Entry(self.frame9, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpatnn.place(x=347, y=100, width=200, height=15)

        # valor
        self.inpvlrn = Entry(self.frame9, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpvlrn.place(x=347, y=120, width=50, height=15)

        # data
        self.inpdatan = Entry(self.frame9, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpdatan.place(x=347, y=140, width=120, height=15)

        # situação
        self.inpsitun = Entry(self.frame9, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpsitun.place(x=347, y=160, width=70, height=15)

    def botaoatagn(self):
        # botao buscar cad
        self.btbusc = Button(self.frame9, text='Buscar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=self.buscaidagn)
        self.btbusc.place(x=82, y=7, width=60, height=15)

        # botao atualizar
        self.btat = Button(self.frame9, text='Atualizar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=self.atagendamento)
        self.btat.place(x=450, y=5, width=100, height=20)

class deletaragn(funcs):
    def __init__(self):
        self.teladeletaragn()
        self.frames()
        self.labels()
        self.inputdel()
        self.botaodel()

    def teladeletaragn(self):
        self.app5 = Toplevel()
        self.app5.title('Deletar Cliente')
        self.app5.geometry('370x210')
        self.app5.resizable(False, False)
        self.app5.iconbitmap(r'mdchefeicon.ico')
        self.app5.configure(background='#CD5C5C')
        self.app5.transient(app)
        self.app5.focus_force()
        self.app5.grab_set()

    def frames(self):
        #bordas do frame
        self.bd = Label(self.app5,background='#000')
        self.bd.place(x=8,y=8,width=353,height=193)
        #frame da tela
        self.frame10 = Frame(self.app5,background='#FFC0CB')
        self.frame10.place(x=10,y=10,width=350,height=190)
        #linha do frame
        self.linha = Label(self.frame10,background='#000')
        self.linha.place(x=5,y=30,width=340,height=2)

    def labels(self):
        # id
        self.lbid = Label(self.frame10, text='Id', font=('calibri', 10, 'bold'), background='#FFC0CB', foreground='#000')
        self.lbid.place(x=7, y=7, width=15, height=15)

        # dados atuais
        self.atual = Label(self.frame10, text='Dados Atuais', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.atual.place(x=100, y=38, width=75, height=15)
        # nome
        self.lbnome = Label(self.frame10, text='Nome do Cliente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbnome.place(x=7, y=60, width=94, height=15)

        # atendente
        self.lbatn = Label(self.frame10, text='Nome do Atendente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbatn.place(x=7, y=80, width=114, height=15)

        # serviço
        self.lbserv = Label(self.frame10, text='Serviço', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbserv.place(x=7, y=100, width=40, height=15)

        # valor
        self.lbvlr = Label(self.frame10, text='Valor R$', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbvlr.place(x=7, y=120, width=45, height=15)

        # data
        self.lbdata = Label(self.frame10, text='Data dd/mm/aa hh:mm', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbdata.place(x=7, y=140, width=130, height=15)

        # situação
        self.lbsitu = Label(self.frame10, text='Situação', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbsitu.place(x=7, y=160, width=45, height=15)
        # --------------------------------------------------------------------------------------------------------------#
        # nome velho
        self.lbnomev = Label(self.frame10, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbnomev.place(x=142, y=60, width=200, height=15)

        # atendente velho
        self.lbatnv = Label(self.frame10, text='', font=('calibri', 10, 'bold'), background='#ffffff', foreground='#000')
        self.lbatnv.place(x=142, y=80, width=200, height=15)

        # serviço velho
        self.lbserv = Label(self.frame10, text='', font=('calibri', 10, 'bold'), background='#ffffff', foreground='#000')
        self.lbserv.place(x=142, y=100, width=100, height=15)

        # valor velho
        self.lbvlrv = Label(self.frame10, text='', font=('calibri', 10, 'bold'), background='#ffffff', foreground='#000')
        self.lbvlrv.place(x=142, y=120, width=50, height=15)

        # data velha
        self.lbdatav = Label(self.frame10, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbdatav.place(x=142, y=140, width=160, height=15)

        # situação velha
        self.lbsituv = Label(self.frame10, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbsituv.place(x=142, y=160, width=195, height=15)

        # dados novos
        self.novo = Label(self.frame10, text='Dados Novos', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.novo.place(x=382, y=40, width=75, height=15)

    def inputdel(self):
        # id busca
        self.inpid = Entry(self.frame10, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpid.place(x=27, y=7, width=50, height=15)

    def botaodel(self):
        #botao buscar cad
        self.btbusc = Button(self.frame10, text='Buscar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=self.buscaidagn)
        self.btbusc.place(x=82,y=7,width=60,height=15)

        #botao deletar cad
        self.btdel = Button(self.frame10, text='Deletar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=self.deletaragn)
        self.btdel.place(x=240,y=5,width=100,height=20)

class cliente(funcs):
    def __init__(self):
        self.telacli()
        self.framecli()
        self.tabelcli()
        self.labelscli()
        self.inputscli()
        self.botoescli()
        self.listacli()

    def telacli(self):
        self.app1 = Toplevel()
        self.app1.title('Clientes')
        self.app1.geometry('500x500')
        self.app1.resizable(False, False)
        self.app1.iconbitmap(r'mdchefeicon.ico')
        self.app1.configure(background='#CD5C5C')
        self.app1.transient(app)
        self.app1.focus_force()
        self.app1.grab_set()

    def framecli(self):
        #bordas
        self.bdcima = Label(self.app1, background='#000')
        self.bdcima.place(x=5,y=5,width=489,height=235)
        self.bdbaixo = Label(self.app1, background='#000')
        self.bdbaixo.place(x=5, y=258, width=489, height=235)

        #frame de cima da tela clientes
        self.frame4 = Frame(self.app1, background='#FFC0CB')
        self.frame4.place(x=7,y=7,width=485,height=230)

        #frame de baixo da tela clientes
        self.frame5 = Frame(self.app1, background='#FFC0CB')
        self.frame5.place(x=7,y=260,width=485,height=230)

        #bordas do frame4
        self.bdmeio = Label(self.frame4, background='#000')
        self.bdmeio.place(x=319,y=29,width=153,height=173)

        #frame dentro do frame4
        self.frame6 = Frame(self.frame4, background='#CD5C5C')
        self.frame6.place(x=320,y=30,width=150,height=170)

        #linhas
        self.linhadecima = Label(self.frame4, background='#000')
        self.linhadecima.place(x=10, y=20, width=465, height=2)
        self.linhadebaixo = Label(self.frame4, background='#000')
        self.linhadebaixo.place(x=10, y=210, width=465, height=2)
        self.linhadomeio = Label(self.frame6, background='#000')
        self.linhadomeio.place(x=5,y=110,width= 139,height=2)

    def tabelcli(self):
        self.tabelacli = ttk.Treeview(self.frame5, height=30, column=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.tabelacli.heading('#0', text='')
        self.tabelacli.heading('#1', text='id')
        self.tabelacli.heading('#2', text='Nome do Cliente')
        self.tabelacli.heading('#3', text='CPF')
        self.tabelacli.heading('#4', text='Telefone')

        self.tabelacli.column('#0', width=1)
        self.tabelacli.column('#1', width=85)
        self.tabelacli.column('#2', width=105)
        self.tabelacli.column('#3', width=100)
        self.tabelacli.column('#4', width=100)

        self.tabelacli.place(x=10, y=10, width=425, height=210)

        self.barrarolagem = Scrollbar(self.frame5, orient='vertical')
        self.tabelacli.configure(yscroll=self.barrarolagem.set)
        self.barrarolagem.place(x=435, y=44, width=32, height=175)

    def labelscli(self):
        #Nome
        self.lbnome = Label(self.frame4, text='Nome do Cliente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbnome.place(x=10, y=55, width=94, height=15)

        #Cpf
        self.lbcpf = Label(self.frame4, text='CPF', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbcpf.place(x=10,y=90,width=20,height=15)

        #telefone
        self.lbtel= Label(self.frame4, text='Telefone', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbtel.place(x=10,y=130,width=48,height=15)

        # id
        self.lbid = Label(self.frame6, text='Id', font=('calibri', 13, 'bold'), background='#CD5C5C', foreground='#000')
        self.lbid.place(x=7, y=125, width=15, height=20)

    def inputscli(self):
        # nome
        self.inpnome = Entry(self.frame4,background='#ffffff',foreground='#000',font=('calibri',10))
        self.inpnome.place(x=109, y=55, width=200, height=15)

        #cpf
        self.inpcpf = Entry(self.frame4,background='#ffffff',foreground='#000',font=('calibri',10))
        self.inpcpf.place(x=35, y=90, width=100, height=15)

        #telefone
        self.inptel = Entry(self.frame4,background='#ffffff',foreground='#000',font=('calibri',10))
        self.inptel.place(x=63, y=130, width=100, height=15)

        # id
        self.inpid = Entry(self.frame6, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpid.place(x=27, y=125, width=50, height=20)

    def botoescli(self):
        #botao cadastra
        self.btcad = Button(self.frame6, text='Cadastrar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=self.cadcli)
        self.btcad.place(x=7, y=7, width=135, height=20)

        # botao atualizar
        self.btatualizar = Button(self.frame6, text='Atualizar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command= atualizarcad)
        self.btatualizar.place(x=7, y=32, width=135, height=20)

        # botao limpar campos
        self.btlimpar = Button(self.frame6, text='Limpar Campos', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command= self.limparcampos2)
        self.btlimpar.place(x=7, y=57, width=135, height=20)

        # botao de deletar
        self.btdelete = Button(self.frame6, text='Deletar Cliente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=deletarcad)
        self.btdelete.place(x=7, y=82, width=135, height=20)

        # BOTAO FILTRO
        self.btfiltro = Button(self.frame6, text='Filtrar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=self.filtrocli)
        self.btfiltro.place(x=82, y=125, width=60, height=20)

        # botao recarregar
        self.photo = PhotoImage(file=r"C:\Users\mayco\Desktop\meu_projeto\refresh.png")
        self.photo1 = self.photo.subsample(13, 13)
        self.brrefresh = Button(self.frame5, image=self.photo1, background='#FFC0CB', foreground='#000',command=self.listacli)
        self.brrefresh.place(x=435, y=10, width=33, height=33)

class atualizarcad(funcs):
    def __init__(self):
        self.atulizarcli()
        self.framesat()
        self.labelsat()
        self.inputat()
        self.botaoat()

    def atulizarcli(self):
        self.app3 = Toplevel()
        self.app3.title('Atualizar Cliente')
        self.app3.geometry('550x180')
        self.app3.resizable(False, False)
        self.app3.configure(background='#CD5C5C')
        self.app3.iconbitmap(r'mdchefeicon.ico')
        self.app3.transient(app)
        self.app3.focus_force()
        self.app3.grab_set()

    def framesat(self):
        #borda do frame
        self.bd = Label(self.app3,background='#000')
        self.bd.place(x=8,y=8,width=534,height=169)

        #frame da tela
        self.frame7 = Frame(self.app3, background='#FFC0CB')
        self.frame7.place(x=10,y=10,width=530,height=165)

        #linha d cima
        self.linhacima =Label(self.frame7,background='#000')
        self.linhacima.place(x=5,y=30,width=518,height=2)

    def labelsat(self):
        # id
        self.lbid = Label(self.frame7, text='Id', font=('calibri', 10, 'bold'), background='#FFC0CB', foreground='#000')
        self.lbid.place(x=7, y=7, width=15, height=15)

        #dados atuais
        self.atual = Label(self.frame7, text='Dados Atuais', font=('calibri', 10, 'bold'), background='#FFC0CB', foreground='#000')
        self.atual.place(x=100,y=40,width=75,height=15)

        #Nome
        self.lbnome = Label(self.frame7, text='Nome do Cliente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbnome.place(x=7, y=70, width=94, height=15)

        # Cpf
        self.lbcpf = Label(self.frame7, text='CPF', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbcpf.place(x=7, y=100, width=20, height=15)

        # telefone
        self.lbtel = Label(self.frame7, text='Telefone', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbtel.place(x=7, y=130, width=48, height=15)

        # Nome velho
        self.lbnome = Label(self.frame7, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbnome.place(x=112, y=70, width=200, height=15)

        # Cpf velho
        self.lbcpf = Label(self.frame7, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbcpf.place(x=112, y=100, width=100, height=15)

        # telefone velho
        self.lbtel = Label(self.frame7, text='', font=('calibri', 10, 'bold'), background='#ffffff',foreground='#000')
        self.lbtel.place(x=112, y=130, width=100, height=15)

        #dados novos
        self.novo = Label(self.frame7, text='Dados Novos', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.novo.place(x=382, y=40, width=75, height=15)

    def inputat(self):
        # id busca
        self.inpid = Entry(self.frame7, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpid.place(x=27, y=7, width=50, height=15)

        # nome novo
        self.inpnomen = Entry(self.frame7, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpnomen.place(x=320, y=70, width=200, height=15)

        # cpf novo
        self.inpcpfn = Entry(self.frame7, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpcpfn.place(x=320, y=100, width=100, height=15)

        # telefone novo
        self.inpteln = Entry(self.frame7, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpteln.place(x=320, y=130, width=100, height=15)

    def botaoat(self):
        #botao buscar cad
        self.btbusc = Button(self.frame7, text='Buscar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command= self.buscacli)
        self.btbusc.place(x=82,y=7,width=60,height=15)

        #botao atualizar
        self.btat = Button(self.frame7, text='Atualizar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=self.atcliente)
        self.btat.place(x=420,y=5,width=100,height=20)

class deletarcad(funcs):
    def __init__(self):
        self.teladeletarcad()
        self.frames()
        self.labelsdel()
        self.inputdel()
        self.botaodel()

    def teladeletarcad(self):
        self.app4 = Toplevel()
        self.app4.title('Deletar Cliente')
        self.app4.geometry('350x150')
        self.app4.resizable(False, False)
        self.app4.iconbitmap(r'mdchefeicon.ico')
        self.app4.configure(background='#CD5C5C')
        self.app4.transient(app)
        self.app4.focus_force()
        self.app4.grab_set()

    def frames(self):
        #bordas do frame
        self.bd = Label(self.app4,background='#000')
        self.bd.place(x=8,y=8,width=329,height=129)
        #frame da tela
        self.frame8 = Frame(self.app4,background='#FFC0CB')
        self.frame8.place(x=10,y=10,width=325,height=125)
        #linha do frame
        self.linha = Label(self.frame8,background='#000')
        self.linha.place(x=5,y=30,width=310,height=2)

    def labelsdel(self):
        # id
        self.lbid = Label(self.frame8, text='Id', font=('calibri', 10, 'bold'), background='#FFC0CB', foreground='#000')
        self.lbid.place(x=7, y=7, width=15, height=15)

        # dados atuais
        self.atual = Label(self.frame8, text='Dados Atuais', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.atual.place(x=100, y=38, width=75, height=15)

        # Nome
        self.lbnome = Label(self.frame8, text='Nome do Cliente', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbnome.place(x=7, y=58, width=94, height=15)

        # Cpf
        self.lbcpf = Label(self.frame8, text='CPF', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbcpf.place(x=7, y=78, width=20, height=15)

        # telefone
        self.lbtel = Label(self.frame8, text='Telefone', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000')
        self.lbtel.place(x=7, y=98, width=48, height=15)

        # Nome velho
        self.lbnome = Label(self.frame8, text='', font=('calibri', 10, 'bold'), background='#ffffff', foreground='#000')
        self.lbnome.place(x=112, y=58, width=200, height=15)

        # Cpf velho
        self.lbcpf = Label(self.frame8, text='', font=('calibri', 10, 'bold'), background='#ffffff', foreground='#000')
        self.lbcpf.place(x=112, y=78, width=100, height=15)

        # telefone velho
        self.lbtel = Label(self.frame8, text='', font=('calibri', 10, 'bold'), background='#ffffff', foreground='#000')
        self.lbtel.place(x=112, y=98, width=100, height=15)

    def inputdel(self):
        # id busca
        self.inpid = Entry(self.frame8, background='#ffffff', foreground='#000', font=('calibri', 10))
        self.inpid.place(x=27, y=7, width=50, height=15)

    def botaodel(self):
        #botao buscar cad
        self.btbusc = Button(self.frame8, text='Buscar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=self.buscacli)
        self.btbusc.place(x=82,y=7,width=60,height=15)

        #botao deletar cad
        self.btdel = Button(self.frame8, text='Deletar', font=('calibri', 10, 'bold'), background='#FFC0CB',foreground='#000',command=self.deletarcli)
        self.btdel.place(x=210,y=5,width=100,height=20)

aplicativo()