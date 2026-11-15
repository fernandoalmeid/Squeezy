<div align="center">

# Squeezy

**Modern archive tool** built with Python and CustomTkinter.

Compress files/folders and extract archives with a clean dark UI and progress bar.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-green?style=flat-square)](https://github.com/TomSchimansky/CustomTkinter)

</div>

---

### Features

- Compress files or entire folders
- Formats: `.7z`, `.zip` (`.rar` falls back to `.7z`)
- Extract `.7z`, `.zip`, `.rar`, `.tar*`
- Animated progress bar
- Clean dark interface

### Requirements

- Python 3.10+
- [7-Zip](https://www.7-zip.org/) in PATH
- `pip install customtkinter`

### How to run

```bash
python squeezy.py
```

### Project structure

```
Squeezy/
├── squeezy.py
└── README.md
```

### Notes

- Real `.rar` creation is not supported by 7-Zip (extraction only)
- Make sure `7z` works in your terminal before running

---

**License:** MIT
