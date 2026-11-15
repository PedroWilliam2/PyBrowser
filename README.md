# 🏴‍☠️ PyBrowser (feat. Grumete)

![PyBrowser Logo](ancora.png)
*(Yes, I made the logo myself. Yes, I know it's ugly. It adds character.)*

**PyBrowser** is a lightweight, simple web browser built entirely in Python. It strips away modern web bloat to give you a fast, no-nonsense browsing experience—assisted by **Grumete** (Portuguese for *cabin boy*, the young sailors who used to help navigate ships back in the day).

---

## 🚫 Why No JavaScript?
Because modern JavaScript turns lightweight browsers into slow, laggy garbage. 

PyBrowser intentionally **does not render JavaScript**. Instead, it focuses on clean HTML/CSS rendering and smart request handling, keeping memory usage low and page loads snappy without heavy browser engines dragging your PC down.

---

## 🛠️ Built With
* **[Tkinter](https://python.org)** – Native Python GUI framework for the browser window and controls.
* **[TkinterWeb](https://pypi.org)** – Lightweight HTML/CSS rendering engine inside Tkinter.
* **[Camoufox](https://github.com)** – Stealthy, anti-detect browser/fetching capabilities under the hood.
* **[Requests](https://pypi.org)** – Clean and simple HTTP requests.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com
cd PyBrowser
```

### 2. Install dependencies
```bash
pip install tkinterweb camoufox requests
```
*(Note: On Linux, you may also need to install `python3-tk` via your system package manager, e.g., `sudo apt install python3-tk`.)*

### 3. Run the browser
```bash
python main.py
```

---

## ⚓ About "Grumete"
In naval history, a **Grumete** was the young crew member learning the ropes and helping navigate the ship. Here, Grumete is your sidekick helping you steer through the web without getting sunk by heavy scripts and trackers.

---

## 📝 License
Do whatever you want with it. Fork it, break it, fix the logo if you dare.
