from camoufox.sync_api import Camoufox
from bs4 import BeautifulSoup
import requests

class Cosa:
    def __init__(self, link="https://info.cern.ch/"):
        self.link = link
        self.html_final = "Erro ao carregar---"

    def req(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36"
            #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(self.link, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for css in soup(["style", "link"]):
            if css.name == "style" or (css.name == "link" and "stylesheet" in str(css.get("rel"))):
                css.decompose()
        return str(soup) 

    def camou(self):
        with Camoufox(
            headless=True, 
            disable_coop=True,
            i_know_what_im_doing=True,
            os="windows"
        ) as browser:
            if self.link:
                c = str(self.link)
                page = browser.new_page()
                page.goto(c)
                page.wait_for_load_state("domcontentloaded", timeout=30000)
                html = page.content()
                page.close()
                soup = BeautifulSoup(html, "html.parser")

                for css in soup(["style", "link"]):
                    if css.name == "style" or (css.name == "link" and "stylesheet" in str(css.get("rel", []))):
                        css.decompose()

                return soup

    def run(self):
        try:
            self.html_final = str(self.req())
        except:
            try:
                self.html_final = str(self.camou())
            except:
                self.html_final = "<html><body><h1>Erro ao carregar o site!</h1>" \
                "<a href='https://html.duckduckgo.com'>Duckduckgo!</a> </body></html>"
