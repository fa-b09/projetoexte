from tkinter import *
from tkinter import ttk
import sqlite3

root  = Tk()


class Funcs():
    
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.quantidade_entry.delete(0, END)
        self.quantidade_dia_entry.delete(0, END)
        self.data_f_entry.delete(0, END)
        self.data_i_entry.delete(0, END)
        self.valor_unitario_entry.delete(0, END)
        self.valor_total_entry.delete(0,END)
    #adicionado
    def concecta_bd(self):
        self.conn = sqlite3.connect('Pds.bd')
        self.cursor = self.conn.cursor()
        print('conectando ao banco de dados')

    def desconecta_bd(self):
        self.conn.close()
        print('Desconectando ao banco de dados')

    def montaTabelas(self):
        self.concecta_bd();
        ## criar tabela
        self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS Pds (
                   cod INTERGER ,
                   nome_cliente CHAR(40)NOT NULL,
                   Quantidade INTERGER(20)NOT NULL,
                   Quantidade_por_dia INTERGER(30)NOT NULL,
                   Data_Inicio DATE NOT NULL,
                   Data_Final DATE NOT NULL);    
        """)
        self.conn.commit();
        print('Banco de dados criado')
        self.desconecta_bd()

    def add_pedido(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.quantidade = self.quantidade_entry.get()
        self.quantidade_por_dia = self.quantidade_dia_entry.get()
        self.data_i = self.data_i_entry.get()
        self.data_f = self.data_f_entry.get()
        self.valor_unitario = self.valor_unitario_entry.get()
        self.valor_total = self.valor_total_entry.get()
        self.concecta_bd()

        self.cursor.execute('INSERT INTO Pds VALUES(?,?,?,?,?,?)',[self.codigo,self.nome, self.quantidade, self.quantidade_por_dia, self.data_i,
                                               self.data_f])  # aspas triplas para usarmos aspas no sql se necessário
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()


    def select_lista(self):
        self.listCli.delete(*self.listCli.get_children())
        self.concecta_bd()
        lista = self.cursor.execute(""" SELECT  cod, nome_cliente,Quantidade,Quantidade_por_dia,Data_Inicio, Data_Final FROM Pds
           ORDER BY nome_cliente ASC;""")
        for i in lista:
            self.listCli.insert("", END, values=i)
        self.desconecta_bd()

    
        

class Application(Funcs):
    def __init__(self):
            self.root = root
            self.tela()
            self.frames_de_tela()
            self.widgests_frame1()
            self.lista_frame2()
            self.montaTabelas()
            self.select_lista()
            self.add_pedido()
            self.limpa_tela()

            root.mainloop()







#adicionado



    def tela(self):
        self.root.title('Cadastro de Pedidos')


        self.root.configure(backgroun="#836FFF")
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)
    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd_=4, bg_="#6959CD",
                            highlightbackground="white", highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.94, relheight=0.46)

        self.frame_2 = Frame(self.root, bd_=4, bg_="white",
                             highlightbackground="white", highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.94, relheight=0.46)
    def widgests_frame1(self):
        #criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text= "Limpar", bd=2 ,bg='#F5FFFA',
                                font=("Arial", 0, "italic" ), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão Buscar
        self.bt_Buscar = Button(self.frame_1, text="Buscar", bd=2 ,bg='#F5FFFA',
                                font=("Arial", 0, "italic"))
        self.bt_Buscar.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão Novo
        self.bt_Novo = Button(self.frame_1, text="Novo", bd=2 ,bg='#F5FFFA',
                                font=("Arial", 0, "italic"), command=self.add_pedido)
        self.bt_Novo.place(relx=0.15, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão Alterar
        self.bt_Alterar = Button(self.frame_1, text="Alterar",bd=2 ,bg='#F5FFFA',
                                font=("Arial", 0, "italic"))
        self.bt_Alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # criação do botão Apagar
        self.bt_Apagar = Button(self.frame_1, text="Apagar", bd=2 ,bg='#F5FFFA',
                                font=("Arial", 0, "italic"))
        self.bt_Apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #botão calcular
        self.bt_calcular = Button(self.frame_1, text="Calcular", bd=2, bg='#F5FFFA',
                                font=("Arial", 0, "italic"))
        self.bt_calcular.place(relx=0.36, rely=0.50, relwidth=0.10, relheight=0.10)

        # criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text="Código", fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.07, relwidth=0.07)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.07)

        # criação da label e entrada do Nome
        self.lb_nome = Label(self.frame_1, text="Nome da peça",fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.18, rely=0.35, relwidth=0.60)

        # criação da label e entrada da quantidade
        self.lb_quantidade = Label(self.frame_1, text="Quantidade por dia", fg='#107db2')
        self.lb_quantidade.place(relx=0.05, rely=0.50, relwidth=0.18)

        self.quantidade_entry = Entry(self.frame_1)
        self.quantidade_entry.place(relx=0.25, rely=0.5, relwidth=0.10)

        self.lb_quantidade_dia = Label(self.frame_1, text="Quantidade", fg='#107db2')
        self.lb_quantidade_dia.place(relx=0.05, rely=0.6, relwidth=0.12)

        self.quantidade_dia_entry = Entry(self.frame_1)
        self.quantidade_dia_entry.place(relx=0.25, rely=0.6, relwidth=0.10)
        
        self.lb_valor_unitario = Label(self.frame_1, text="Valor_unitário", fg='#107db2')
        self.lb_valor_unitario.place(relx=0.05, rely=0.7, relwidth=0.12)

        self.valor_unitario_entry = Entry(self.frame_1)
        self.valor_unitario_entry.place(relx=0.25, rely=0.7, relwidth=0.10)



        # criação da label e entrada da data
        self.lb_data_i= Label(self.frame_1, text="Data Inicio", fg='#107db2')
        self.lb_data_i.place(relx=0.05, rely=0.8, relwidth=0.12)

        self.data_i_entry = Entry(self.frame_1)
        self.data_i_entry.place(relx=0.25, rely=0.8, relwidth=0.1)

        self.lb_data_f = Label(self.frame_1, text="Data Fim", fg='#107db2')
        self.lb_data_f.place(relx=0.05, rely=0.9, relwidth=0.12)

        self.data_f_entry = Entry(self.frame_1)
        self.data_f_entry.place(relx=0.25, rely=0.9, relwidth=0.10)
        
        # BOTÃO VALOR TOTAL
        
        
        self.bt_Valor_total = Button(self.frame_1, text="Valor Total", bd=2, bg='#F5FFFA',
                                font=("Arial", 0, "italic"))
        self.bt_Valor_total.place(relx=0.60, rely=0.9, relwidth=0.17, relheight=0.10)
        
        self.valor_total_entry = Entry(self.frame_1)
        self.valor_total_entry.place(relx=0.77, rely=0.9, relwidth=0.10)

    def lista_frame2(self):
        self.listCli = ttk.Treeview(self.frame_2, height=3, colum=('col1', 'col2', 'col3', 'col4','col5','col6', 'col7','col8'))
        self.listCli.heading("#0", text='')
        self.listCli.heading('#1', text='Código')
        self.listCli.heading('#2', text='Nome')
        self.listCli.heading('#3', text='Quantidade')
        self.listCli.heading('#4', text='Quantidade por dia')
        self.listCli.heading('#5', text='Data inicio')
        self.listCli.heading('#6', text='Data Final')
        self.listCli.heading('#7', text='Valor_unitario')
        self.listCli.heading('#8', text='Valor_total')

        self.listCli.column('#0', width=1)
        self.listCli.column('#1', width=30)
        self.listCli.column('#2', width=150)
        self.listCli.column('#3', width=100)
        self.listCli.column('#4', width=100)
        self.listCli.column('#5', width=100)
        self.listCli.column('#6', width=100)
        self.listCli.column('#7', width=100)
        self.listCli.column('#8', width=100)

        self.listCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        # Barra de rolagem
        self.scrollista = Scrollbar(self.frame_2, orient='vertical')
        self.listCli.configure(yscroll=self.scrollista.set)
        self.scrollista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

Application()