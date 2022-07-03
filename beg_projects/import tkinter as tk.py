from pydoc import synopsis
import tkinter as tk
from matplotlib.pyplot import title 
import pandas as pd
import pymysql

class book:
    def __init__(self, title, pages, wikipedia_link, synopsis):
        self.title = title
        self.pages = pages 
        self.wikipedia_link = wikipedia_link
        self.synopsis = synopsis 


hrry_pttr = book('Harry Potter y su puta madre con bigote', 367, 'https://es.wikipedia.org/wiki/Harry_Potter', 'Harry Potter es un hijo de puta')
# 

