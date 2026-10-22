import subprocess
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox

class ArchiveApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Squeezy")
        self.geometry("500x340")
        self.resizable(False, False)

        self.compress_btn = ctk.CTkButton(
            self, text="Compress Folder/Files", command=self.compress
        )
        self.compress_btn.pack(pady=(30, 10))

        self.extract_btn = ctk.CTkButton(
            self, text="Extract Archive", command=self.extract
        )
        self.extract_btn.pack(pady=10)

        self.progress = ctk.CTkProgressBar(self, width=300, mode="indeterminate")
        self.progress.pack(pady=20)
        self.progress.pack_forget()          

        self.status = ctk.CTkLabel(self, text="")
        self.status.pack(pady=5)

    def set_busy(self, busy: bool, message: str = ""):
        """Enable/disable buttons + show/hide progress bar"""
        state = "disabled" if busy else "normal"
        self.compress_btn.configure(state=state)
        self.extract_btn.configure(state=state)

        if busy:
            self.progress.pack(pady=20)
            self.progress.start()
            self.status.configure(text=message)
        else:
            self.progress.stop()
            self.progress.pack_forget()
            self.status.configure(text=message)

    def compress(self):
        choice = messagebox.askyesnocancel(
            "Compress",
            "Yes = Select Files\nNo = Select Folder\nCancel = Abort"
        )

        if choice is None:
            return
        elif choice:  
            selected = filedialog.askopenfilenames(title="Select Files to Compress")
            if not selected:
                return
            items = list(selected)
        else:  
            folder = filedialog.askdirectory(title="Select Folder to Compress")
            if not folder:
                return
            items = [folder]

        output_file = filedialog.asksaveasfilename(
            defaultextension=".7z",
            filetypes=[
                ("7z Archive", "*.7z"),
                ("Zip Archive", "*.zip"),
                ("RAR Archive", "*.rar"),
            ],
            title="Save Compressed File As",
        )
        if not output_file:
            return

        lower = output_file.lower()
        if lower.endswith(".7z"):
            cmd = ["7z", "a", output_file] + items
        elif lower.endswith(".zip"):
            cmd = ["7z", "a", "-tzip", output_file] + items
        else:
            messagebox.showwarning(
                "Format",
                "7-Zip cannot create real .rar files.\nSaving as .7z instead."
            )
            if not lower.endswith(".7z"):
                output_file = output_file.rsplit(".", 1)[0] + ".7z"
            cmd = ["7z", "a", output_file] + items

        self.set_busy(True, "Compressing... please wait")
        threading.Thread(
            target=self._run_command,
            args=(cmd, "Compressed successfully!"),
            daemon=True
        ).start()

    def extract(self):
        archive = filedialog.askopenfilename(
            filetypes=[("Archives", "*.7z *.zip *.rar *.tar*")]
        )
        if not archive:
            return

        dest = filedialog.askdirectory(title="Select Extract Folder")
        if not dest:
            return

        cmd = ["7z", "x", archive, f"-o{dest}", "-y"]

        self.set_busy(True, "Extracting... please wait")
        threading.Thread(
            target=self._run_command,
            args=(cmd, "Extracted successfully!"),
            daemon=True
        ).start()

    def _run_command(self, cmd, success_msg):
        try:
            subprocess.run(cmd, check=True)
            # Back to main thread to update UI
            self.after(0, lambda: self._on_success(success_msg))
        except Exception as e:
            self.after(0, lambda: self._on_error(str(e)))

    def _on_success(self, msg):
        self.set_busy(False, "")
        messagebox.showinfo("Done", msg)

    def _on_error(self, error):
        self.set_busy(False, "")
        messagebox.showerror("Error", error)


if __name__ == "__main__":
    app = ArchiveApp()
    app.mainloop()