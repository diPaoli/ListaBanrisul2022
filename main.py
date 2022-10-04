from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App


tx = TextInput(size_hint=[200, None])
txLog = TextInput()
bt = Button(text="Gerar Lista", bold=True, size_hint=[80,None])
layout = GridLayout()

def build():
    bt.on_press = gerar_lista

    layout.rows = 3
    layout.cols = 1
    layout.add_widget(tx)
    layout.add_widget(bt)
    layout.add_widget(txLog)
    
    return layout


def gerar_lista():
    lista_candidatos = str(tx.text).split('/')
    regs = dict()
    for item in lista_candidatos:
        item = item.replace('\n','')
        nome = item.split(',')[1].strip()
        nota = item.split(',')[6].strip()
        regs.update({nome: nota})
    
    regs = sorted(regs.items(), key=lambda item: item[1], reverse=True)

    pos = 1
    with open('./Lista_Banrisul.txt', encoding='utf-8', mode='w') as file:
        for i in regs:
            line_text = str(f"{pos}: {i[0]} - {i[1]}\n")
            file.write(line_text)
            pos += 1
    
    with open('./Lista_Banrisul.txt', encoding='utf-8', mode='r') as file:
        txLog.text = file.read()
        
        
    
    
    
    
    
    


app = App()
app.build = build
app.title = "Lista de Classificação"
app.run()


