#coding: utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput
import kivymd


def build():
    return TextInput(text="Componente TextInput")

janela = App()
janela.build = build
janela.run()
