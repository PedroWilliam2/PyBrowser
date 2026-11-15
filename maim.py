import requests
import sys
import os
from bs4 import BeautifulSoup
import tkinter as tk
from tkinterweb import HtmlFrame
from navegador import *
from PIL import Image, ImageTk 
from tkinter import ttk
import threading

def arrumar_caminho(caminho_relativo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, caminho_relativo)
    return os.path.join(os.path.abspath("."), caminho_relativo)


html_base = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GO DRINK VAI TOMANDO</title>
</head>

<body>
    <h3>Search engines: </h3>
    <ul>
        <li><a href="https://html.duckduckgo.com">DuckDuckGo - 👑</a>
    </li>
    <li><a href="https://google.com">Google</a></li>
    <li><a href="https://mojeek.com">Mojeek</a></li>
    <li><a href="https://brave.com">Brave</a></li>
    </ul>
    <h3>Information and news: </h3>
    <ul>
        <li><a href="https://wikipedia.org">Wikipedia</a></li>
        <li><a href="https://globo.com">G1 Noticias - to Brazil</a></li>
    </ul>
</body>

</html>
"""

class Nave(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"Grumete")
        self.geometry("800x800")
        self.configure(bg="#949494")
        img_original = Image.open(arrumar_caminho("ancora.png"))
        user_agent_celular = "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36"
        img_redimensionada = img_original.resize((32, 32), Image.Resampling.LANCZOS)
        self.logo_janela = ImageTk.PhotoImage(img_redimensionada)
        self.iconphoto(False, self.logo_janela)

        self.historico_passado = []
        self.historico_futuro = []
        self.url_atual = ""

        self.parada = tk.Frame(self, width=780, height=40, bg="#3149CF", relief="groove")
        
        self.btn_voltar = tk.Button(self.parada, text="⬅️", command=self.voltar, font=("Helvetica", 10))
        self.btn_voltar.pack(pady=5, padx=2, side="left")
        
        self.btn_avancar = tk.Button(self.parada, text="➡️", command=self.avancar, font=("Helvetica", 10))
        self.btn_avancar.pack(pady=5, padx=2, side="left")
        
        txt = tk.Label(self.parada, text="Enter the URL:", background="#3149CF", font="Helvetica", fg="white")
        txt.pack(pady=5, padx=5, side="left")
        
        self.inpt = tk.Entry(self.parada, font=("Helvetica", 12))
        self.inpt.pack(pady=5, padx=5, side="left", ipadx=50, ipady=5, fill="x", expand=True)
        
        self.btn = tk.Button(self.parada, text="Go to", command=self.receba, font=("Helvetica", 10))
        self.btn.pack(pady=5, padx=10, ipady=2, side="left")
        lista = ["?"]
        self.options = ttk.Combobox(self.parada, values=lista, state="readonly", font=("Helvetica", 10))
        self.options.pack(pady=7, padx=4, ipady=2, ipadx=10)
        self.options.current(0)
        self.site = tk.Frame(self)
        
        self.scroll = tk.Scrollbar(self.site)
        self.scroll.pack(side="right", fill="y")
        
        self.textotodofih = HtmlFrame(self.site, on_link_click=self.interceptar_clique)
        self.textotodofih.load_html(str(html_base), base_url=html_base)

        self.textotodofih.pack(side="left", fill="both", expand=True, pady=10, padx=10)
        
        self.scroll.config(command=self.textotodofih.yview)
        
        self.parada.pack(fill="x")
        self.site.pack(pady=6, padx=4, fill="both", expand=True)

    def receba(self):
        url = self.inpt.get().lower().strip()
        self.receba_url(url, limpar_futuro=True)

    def interceptar_clique(self, url):
        self.receba_url(url.lower().strip(), limpar_futuro=True)
        return "break"

    def receba_url(self, url, limpar_futuro=False):
        if url.startswith("https://") or url.startswith("http://"):
            if self.url_atual and self.url_atual != url:
                self.historico_passado.append(self.url_atual)
                if limpar_futuro:
                    self.historico_futuro.clear()
            
            self.url_atual = url
            self.inpt.delete(0, tk.END)
            self.inpt.insert(0, url)
            
            threading.Thread(target=self._tarefa_carregamento_assincrono, args=(url,), daemon=True).start()
        else:
            self.url_atual = ""
            self.inpt.delete(0, tk.END)
            self.textotodofih.load_html(str(html_base), base_url=html_base)

    def _tarefa_carregamento_assincrono(self, url):
        pagina = Cosa(url)
        pagina.run()
        codigo_html = str(pagina.html_final)
        self.textotodofih.load_html(codigo_html, base_url=url)

    def voltar(self):
        if self.historico_passado:
            url_anterior = self.historico_passado.pop()
            if self.url_atual:
                self.historico_futuro.append(self.url_atual)
            self.receba_url(url_anterior, limpar_futuro=False)

    def avancar(self):
        if self.historico_futuro:
            url_seguinte = self.historico_futuro.pop()
            if self.url_atual:
                self.historico_passado.append(self.url_atual)
            self.receba_url(url_seguinte, limpar_futuro=False)

janela = Nave()
janela.mainloop()
