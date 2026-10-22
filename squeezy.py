import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

class ArchiveApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Squeezy")
        self.geometry("500x300")

        ctk.CTkButton(self, text="Compress Folder/Files", command=self.compress).pack(pady=20)
        ctk.CTkButton(self, text="Extract Archive", command=self.extract).pack(pady=10)

    def compress(self):
        files = filedialog.askopenfilenames() or [filedialog.askdirectory()]
        if not files:
            return
        output = filedialog.asksaveasfilename(defaultextension=".7z",
                                             filetypes=[("7z archive", "*.7z"), ("ZIP", "*.zip")])
        if not output:
            return

        cmd = ["7z", "a", "-t7z", output] + list(files)
        try:
            subprocess.run(cmd, check=True)
            messagebox.showinfo("Done", f"Created: {output}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def extract(self):
        archive = filedialog.askopenfilename(filetypes=[("Archives", "*.7z *.zip *.rar *.tar*")])
        if not archive:
            return
        dest = filedialog.askdirectory()
        if not dest:
            return

        cmd = ["7z", "x", archive, f"-o{dest}", "-y"]
        try:
            subprocess.run(cmd, check=True)
            messagebox.showinfo("Done", "Extracted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = ArchiveApp()
    app.mainloop()