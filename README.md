# PyCalc (exe Practice Project)

This project is a simple **Python calculator (PyCalc)** built with `tkinter` and packaged into a **standalone .exe file** using `PyInstaller`.  
The purpose of this project is to practice creating `.exe` applications from Python scripts.

---

## 📂 Project Structure
```
py-calc/
 ├─ src/                 # Source code
 │   └─ main.py          # Entry point (calculator app)
 ├─ assets/              # Static files (icons, etc.)
 │   └─ app.ico          # App icon (optional)
 ├─ requirements.txt     # Dependency list
 ├─ .vscode/settings.json# VSCode/Cursor settings (optional)
 └─ README.md            # Documentation
```

---

## 🚀 Run in Development

1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Run the app:
   ```powershell
   python src\main.py
   ```

---

## 📦 Build as exe

1. Install PyInstaller:
   ```powershell
   pip install pyinstaller
   ```

2. Build the executable:
   ```powershell
   pyinstaller `
      --onefile `
      --windowed `
      --name "PyCalc" `
      --icon "assets\app.ico" `
      --add-data "assets\app.ico;assets" `
      src\main.py
   ```

3. Result:
   - The built `.exe` file will be located in the `dist/` folder:
     ```
     dist/PyCalc.exe
     ```

---

## 📝 Notes
- The icon (`app.ico`) is optional. You must use a valid `.ico` file if you want to include it.
- This repository is intended **for practice purposes only**.
