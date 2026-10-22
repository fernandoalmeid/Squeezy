# Squeezy

A simple, modern archive tool built with Python and CustomTkinter.  
Compress files/folders and extract archives with a clean dark UI, progress bar

![Squeezy](https://img.shields.io/badge/Python-3.10%2B-blue)  
![UI](https://img.shields.io/badge/UI-CustomTkinter-green)

---

## Features

- **Compress** files or entire folders
- Supported formats: `.7z`, `.zip` (`.rar` falls back to `.7z`)
- **Extract** `.7z`, `.zip`, `.rar`, `.tar*` archives
- Animated progress bar while working

---

## Requirements

- Python 3.10 or higher
- [7-Zip](https://www.7-zip.org/) installed and available in PATH
- Python packages:

```bash
pip install customtkinter
```

> **Note:** On Windows, after installing 7-Zip, restart your terminal/editor so the `7z` command is recognized.

---

## How to Run

```bash
python squeezy.py
```

---

## How to Use

### Compress
1. Click **Compress Folder/Files**
2. Choose **Yes** for files or **No** for a folder
3. Select what you want to compress
4. Choose where to save the archive (`.7z` or `.zip` recommended)
5. Wait for the progress bar 

### Extract
1. Click **Extract Archive**
2. Select the archive file
3. Choose the destination folder
4. Wait for extraction 

---

## Project Structure

```
Squeezy/
├── squeezy.py      # Main application
└── README.md       # This file
```

---

## Notes

- Real `.rar` creation is **not supported** by 7-Zip (it can only extract RAR).  
  If you choose `.rar`, Squeezy automatically falls back to `.7z`.
- Make sure `7z` works in your terminal before running the app:
  ```bash
  7z
  ```

---

## License

MIT — feel free to use and modify.
