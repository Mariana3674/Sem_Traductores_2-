from tkinter import *
from tkinter import ttk

# Creación de la ventana 1 (Léxico).
g_Lex = Tk()
g_Lex.title('Analizador Léxico')
g_Lex.config(bg="lightblue")  # Color de fondo de la ventana

# Frame
style_lex_frame = ttk.Style()
style_lex_frame.configure('LexFrame.TFrame', background='lightblue')

frm = ttk.Frame(g_Lex, padding=200, style='LexFrame.TFrame')
frm.grid(row=0, column=0)

bold_font = ('Helvetica', 10, 'bold')

# Tabla
tab = ttk.Treeview(frm, columns=("c1", "c2")) # Análisis léxico
tab.grid(row=0, column=0, columnspan=3)
tab.heading("#0", text="Lexema")
tab.heading("c1", text="Token")
tab.heading("c2", text="Tipo")
label2 = Label(g_Lex,text="Analisis Léxico",bg="lightblue", font=bold_font) 
label2.place(x=460, y=430, height=40)
txtE = Text(g_Lex, width=40) 
txtE.place(x=52, y=10, height=150)
label = Label(g_Lex,text="Entrada",bg="lightblue", font=bold_font) # TextBox Entrada
label.place(x=170, y=160, height=40)

# Creación de la ventana 2 (Sintáctico).
g_Sint = Tk()
g_Sint.title('Analizador Sintáctico')
g_Sint.minsize(1400, 1000)
g_Sint.config(bg="lightblue")  # Color de fondo de la ventana
txtE2 = Text(g_Sint, width=144, height=20) # Pila
txtE2.place(x=22, y=10)
label3 = Label(g_Sint,text="Analisis Sintáctico",bg="lightblue", font=bold_font)
label3.place(x=600, y=355, height=40)
txtE3 = Text(g_Sint, width=20, height=20) # Salida
txtE3.place(x=1190, y=10)
label4 = Label(g_Sint,text="Salida",bg="lightblue", font=bold_font) 
label4.place(x=1230, y=355, height=40)
txtE4 = Text(g_Sint, width=130, height=35) # Árbol sintáctico
txtE4.place(x=200, y=390)
label5 = Label(g_Sint,text="Árbol ---->", bg="lightblue", font=bold_font) 
label5.place(x=100, y=570, height=40)

# Creación de la ventana 3 (Análisis semántico).
g_Sem = Tk()
g_Sem.title('Analizador Semántico')
g_Sem.config(bg="lightblue")  # Color de fondo de la ventana

# Frame
style_sem_frame = ttk.Style()
style_sem_frame.configure('SemFrame.TFrame', background='lightblue')

frmS = ttk.Frame(g_Sem, padding=200, style='SemFrame.TFrame')
frmS.grid(row=0, column=0)

# Tabla
tabS = ttk.Treeview(frmS, columns=("c1", "c2"))

tabS.grid(row=0, column=0, columnspan=3)
tabS.heading("#0", text="Tipo")
tabS.heading("c1", text="Identificador")
tabS.heading("c2", text="Ámbito")
labelS = Label(g_Sem, text="Analisis Semántico", bg="lightblue", font=bold_font) # Tabla de símbolos
labelS.place(x=460, y=430, height=40)