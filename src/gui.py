import tkinter as tk
from tkinter import messagebox, filedialog
from downloader import download_video, download_vimeo_video
import os
from dotenv import load_dotenv
import re
import json

load_dotenv()

save_path = os.getenv("SAVE_PATH", "downloads/")  # Definindo valor padrão

HISTORY_FILE = 'download_history.json'

def is_valid_url(url):
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$'
    )
    vimeo_regex = re.compile(
        r'^(https?://)?(www\.)?(vimeo)\.com/.+$'
    )
    return re.match(youtube_regex, url) is not None or re.match(vimeo_regex, url) is not None

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self, text="URL do Vídeo:")
        self.url_label.pack(pady=5)

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=5)

        self.save_label = tk.Label(self, text="Salvar em:")
        self.save_label.pack(pady=5)

        self.save_entry = tk.Entry(self, width=50)
        if save_path:  # Verifica se save_path não é nulo
            self.save_entry.insert(0, save_path)
        self.save_entry.pack(pady=5)

        self.browse_button = tk.Button(self, text="Procurar", command=self.browse_folder)
        self.browse_button.pack(pady=5)

        self.download_button = tk.Button(self, text="Download", command=self.start_download)
        self.download_button.pack(pady=10)

        self.progress = tk.Label(self, text="", fg="green")
        self.progress.pack(pady=5)

        self.history_button = tk.Button(self, text="Ver Histórico", command=self.show_history)
        self.history_button.pack(pady=5)

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom", pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.save_entry.delete(0, tk.END)
            self.save_entry.insert(0, folder_selected)

    def start_download(self):
        url = self.url_entry.get()
        save_path = self.save_entry.get()
        if not is_valid_url(url):
            messagebox.showwarning("Aviso", "Por favor, insira uma URL válida do YouTube ou Vimeo.")
            return
        if url and save_path:
            try:
                self.progress.config(text="Baixando...")
                self.update_idletasks()
                if 'youtube' in url or 'youtu.be' in url:
                    download_video(url, save_path)
                elif 'vimeo' in url:
                    download_vimeo_video(url, save_path)
                self.progress.config(text="Download concluído!")
            except Exception as e:
                self.progress.config(text="")
                messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {e}")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira uma URL e o caminho de salvamento.")

    def show_history(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as file:
                history = json.load(file)
                history_str = "\n".join([f"{item['title']} - {item['url']} - {item['path']}" for item in history])
                messagebox.showinfo("Histórico de Downloads", history_str)
        else:
            messagebox.showinfo("Histórico de Downloads", "Nenhum histórico encontrado.")

def run_app():
    root = tk.Tk()
    root.geometry("500x300")
    root.title("YouTube & Vimeo Video Downloader")
    app = Application(master=root)
    app.mainloop()
