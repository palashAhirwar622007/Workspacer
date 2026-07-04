<div align="center">

# 🚀 Workspacer

**A sleek, interactive Python CLI tool for Windows that lets you save, edit, and instantly launch custom desktop workspaces.**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org)
[![OS](https://img.shields.io/badge/OS-Windows-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Tired of opening the same 5 applications every time you sit down to code, game, or study? **Workspacer** takes a snapshot of your currently running apps and lets you restore them all with a single command.

</div>

---

## ✨ Features

- **Named Workspaces:** Create multiple distinct workspaces (e.g., "Coding", "Gaming", "Editing") saved dynamically to a local `saves/` folder.
- **Interactive Menus:** Built with `questionary` for smooth, arrow-key navigation. No clunky text typing required.
- **Beautiful Terminal UI:** Styled with `rich` to provide clean tables, color-coded text, and clear visual feedback.
- **Smart App Filtering:** Hooks into the Windows API to automatically ignore invisible background processes and system apps, keeping your saves perfectly clean.
- **Edit on the Fly:** View your saved workspaces in a neat table and easily remove specific apps by their serial number without having to recreate the entire workspace.

---

## 🛠️ Prerequisites

- **Operating System:** Windows (Relies on `pywin32` for window management)
- **Python:** Version 3.6 or higher

---

## 📦 Installation

**1. Clone the repository:**

```bash
git clone [https://github.com/palashAhirwar622007/workspacer.git](https://github.com/palashAhirwar622007/workspacer.git)
cd workspacer
```

**2. Install the required dependencies:**
This project relies on a few external Python libraries. Install them via pip:

```bash
pip install psutil rich questionary pywin32
```

---

## 💻 Usage

You can run the script directly using Python from inside the project folder:

```bash
python main.py YourName
```

### 🌍 Make it a Global Command (Recommended)

To run Workspacer from anywhere on your computer without navigating to the project folder, set up a global command:

1. Create a file named `workspacer.bat` inside your project directory and add this code:
   ```bat
   @echo off
   python "C:\Absolute\Path\To\Your\workspacer\main.py" %*
   ```
   _(Be sure to replace the path above with your actual absolute path to `main.py`)_
2. Add your project folder to your Windows **System PATH** Environment Variables.
3. Open a new terminal from anywhere and simply type:
   ```bash
   workspacer Palash
   ```

---

## 📂 Project Structure

| File/Folder   | Description                                                                                 |
| :------------ | :------------------------------------------------------------------------------------------ |
| `main.py`     | The main entry point containing the interactive menu loop and UI.                           |
| `getApps.py`  | Interacts with the Windows API to fetch visible windows and extract their executable paths. |
| `openApps.py` | Handles reading your saved `.txt` files and launching the executables via `subprocess`.     |
| `saves/`      | A dynamically generated folder where all your custom named workspaces are stored.           |

---

## 🤝 Contributing

Contributions, issues, and feature requests are always welcome!
Feel free to check the [issues page](https://github.com/palashAhirwar622007/workspacer/issues) if you want to contribute.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

<!-- https://github.com/palashAhirwar622007/Workspacer.git -->
