#coding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

def click():
    print ("Voce clicou no botão")

def build():
    bt = Button(text="Clique aqui")
    bt.on_press = click
    return bt

janela = App()
janela.build = build
janela.run()
