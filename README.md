# 🏴‍☠️ Grumete

![Grumete Logo](logo.png)

*Yes, I made the logo myself. Yes, I know it's ugly. It adds character.*

**Grumete** is a lightweight, simple web browser built with Python. It strips away modern web bloat to provide a simple browsing experience, with a focus on lightweight HTML/CSS rendering and HTTP request handling.

Grumete (Portuguese for *cabin boy*) refers to the young sailors who helped navigate ships back in the day.

---

## 🚫 Why No JavaScript?

Because modern JavaScript can turn lightweight browsers into slow, resource-hungry applications.

Grumete intentionally **does not execute JavaScript in its TkinterWeb rendering component**. Instead, it focuses on HTML/CSS rendering and HTTP request handling, avoiding the overhead of a full browser engine.

This means some modern websites may not work as expected, especially those heavily dependent on JavaScript.

---

## 🛠️ Built With

- **[Python](https://www.python.org/)** – Main programming language.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)** – GUI framework for the browser window and controls.
- **[TkinterWeb](https://pypi.org/project/tkinterweb/)** – Lightweight HTML/CSS rendering inside Tkinter.
- **[Camoufox](https://github.com/daijro/camoufox)** – Browser automation and page retrieval fallback.
- **[Requests](https://requests.readthedocs.io/)** – HTTP requests.
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** – HTML parsing.
- **[Pillow](https://python-pillow.org/)** – Image processing.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/PedroWilliam2/PyBrowser.git
cd PyBrowser
```

### 2. Create a virtual environment (recommended)

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Camoufox browser

```bash
python -m camoufox fetch
```

### 5. Run Grumete

```bash
python maim.py
```

**Linux note:** You may need to install Tkinter separately:

```bash
sudo apt install python3-tk
```

---

## ⚓ About the Name

In naval history, a **Grumete** was a young crew member learning the ropes and helping navigate ships.

The browser carries that name as a little tribute to those sailors.

---

## 📝 License

No license has been specified yet.
