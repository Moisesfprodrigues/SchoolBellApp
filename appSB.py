#Author App created by Moisés Rodrigues
#Email: moisesrodrigues@gmail.com
#Version: 1.0 | 2024

import RPi.GPIO as GPIO
import tkinter as tk
from datetime import datetime
from time import sleep
import pickle #v1.1 p/ serialização
import PIL
from PIL import ImageTk, Image
import webbrowser

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

# Lista de horários
horarios = ['08:30:00', '10:30:00', '10:45:00', '12:45:00', '13:00:00', '14:00:00', '15:30:00', '17:30:00' ,]

# Função para ativar o GPIO por 3 segundos
def ativar_gpio():
    GPIO.output(12, GPIO.HIGH)
    janela.after(3000, desativar_gpio)

# Função para desativar o GPIO
def desativar_gpio():
    GPIO.output(12, GPIO.LOW)

# Função para atualizar o tempo na label
def atualizar_tempo():
    tempo_atual = datetime.now().strftime('%H:%M:%S')
    tempo_label.config(text='Relógio: ' + tempo_atual)
    tempo_label.after(1000, atualizar_tempo)

# Função para adicionar horário
def adicionar_horario():
    horario = horario_entry.get()
    horarios.append(horario)
    horarios_listbox.insert(tk.END, horario)
    horario_entry.delete(0, tk.END)

# Função para remover horário
def remover_horario():
    horario_selecionado = horarios_listbox.curselection()
    if horario_selecionado:
        horarios_listbox.delete(horario_selecionado[0])
        horarios.pop(horario_selecionado[0])

# Função para verificar horários
def verificar_horarios():
    tempo_atual = datetime.now().strftime('%H:%M:%S')
    if tempo_atual in horarios:
        ativar_gpio()
    janela.after(1000, verificar_horarios)                               

# Função para adicionar link
def abrir_pagina_web():
    webbrowser.open_new_tab('https://mpromaker.com')
        
# Criação da janela
janela = tk.Tk()
janela.title('Campainha Automática')
janela.geometry('300x540')

# Criação dos widgets
imagem = ImageTk.PhotoImage(Image.open('bell.png'))
imagem_label = tk.Label(janela, image=imagem)
espacamento1_label = tk.Label(janela, text='', height=1)
espacamento2_label = tk.Label(janela, text='', height=1)
espacamento3_label = tk.Label(janela, text='', height=1)
ativar_button = tk.Button(janela, bg='#00FA9A', text='Ativar GPIO', command=ativar_gpio)
desativar_button = tk.Button(janela, bg='#F08080', text='Desativar GPIO', command=desativar_gpio)
tempo_label = tk.Label(janela, text=datetime.now().strftime('%H:%M:%S'))
horario_label = tk.Label(janela, text='Insira o horário (HH:MM:SS):')
horario_entry = tk.Entry(janela)
adicionar_button = tk.Button(janela, text='Adicionar horário', command=adicionar_horario)
remover_button = tk.Button(janela, text='Remover horário', command=remover_horario)
horarios_label = tk.Label(janela, text='Lista de Horários:')
horarios_listbox = tk.Listbox(janela, bg='#FFFFCC')
link_label = tk.Label(janela, text='App developed by MPRO@2024', fg='blue', cursor='hand2')

# Posicionamento dos widgets
imagem_label.pack()
espacamento1_label.pack()
ativar_button.pack()
desativar_button.pack()
espacamento2_label.pack()
tempo_label.pack()
horario_label.pack()
horario_entry.pack()
adicionar_button.pack()
remover_button.pack()
espacamento3_label.pack()
horarios_label.pack()
horarios_listbox.pack()
link_label.pack()
link_label.bind('<Button-1>', lambda e: abrir_pagina_web())

for horario in horarios:
    horarios_listbox.insert(tk.END, horario)

# Atualização do tempo
atualizar_tempo()

# Verificação dos horários
verificar_horarios()

# Inicialização da janela
janela.mainloop()


