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
        choice = messagebox.askyesnocancel(
            "Compress",
            "Yes = Select Files\nNo = Select Folder\nCancel = Abort"
        )

        if choice is None:          # Cancel
            return
        elif choice:                # Yes → files
            selected = filedialog.askopenfilenames(title="Select Files to Compress")
            if not selected:
                return
            items = list(selected)
        else:                       # No → folder
            folder = filedialog.askdirectory(title="Select Folder to Compress")
            if not folder:
                return
            items = [folder]

        output_file = filedialog.asksaveasfilename(
            defaultextension=".7z",
            filetypes=[
                ("7z Archive", "*.7z"),
                ("Zip Archive", "*.zip"),
                ("RAR Archive", "*.rar"),  # note: 7-Zip cannot create real RAR
            ],
            title="Save Compressed File As",
        )
        if not output_file:
            return

        lower = output_file.lower()
        if lower.endswith(".7z"):
            cmd = [r"C:\Program Files\7-Zip\7z.exe", "a", output_file] + items
        elif lower.endswith(".zip"):
            cmd = ["7z", "a", "-tzip", output_file] + items
        else:
            # 7-Zip cannot write real RAR files
            messagebox.showwarning(
                "Format",
                "7-Zip cannot create real .rar files.\nSaving as .7z instead."
            )
            if not lower.endswith(".7z"):
                output_file = output_file.rsplit(".", 1)[0] + ".7z"
            cmd = [r"C:\Program Files\7-Zip\7z.exe", "a", output_file] + items

        try:
            subprocess.run(cmd, check=True)
            messagebox.showinfo("Done", "Compressed successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def extract(self):
        archive = filedialog.askopenfilename(
            filetypes=[("Archives", "*.7z *.zip *.rar *.tar*")]
        )
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