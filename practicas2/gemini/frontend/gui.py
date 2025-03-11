import os
from tkinter import scrolledtext, filedialog
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from antlr4 import InputStream, CommonTokenStream
from lib.api_connection import api_connection


class GuiTerminal(tk.Tk):
    def __init__(self, *args):
        title, size = args
        super().__init__()

        self.title(title)
        self.geometry(size)
        self.configure(bg='#1a1b2f')
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.current_scale = 1.0
        self.csv_data = None

        self.create_widgets()

    def load_image(self, image_name, size=(20, 20)):
        file_path = os.path.dirname(os.path.realpath(__file__))
        img_path = os.path.join(file_path, image_name)

        if os.path.exists(img_path):
            img_file = Image.open(img_path)
            img_file = img_file.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img_file)
        else:
            return None

    def create_widgets(self):
        self.img_browser = self.load_image("folder-browser.png")
        self.img_analyse = self.load_image("analyse-file.png")
        self.img_save_file = self.load_image("save-file.png")

        buttons_frame = tk.Frame(self, bg='#1a1b2f')
        buttons_frame.grid(row=0, column=0, sticky="n", padx=10, pady=(10, 5))

        # Botón Analyze con imagen
        button_execute = tk.Button(
            buttons_frame,
            text='Send',
            command=self.validate_text,
            image=self.img_analyse,
            compound=LEFT,
            bg='#6a5acd',
            fg='#dcdcdc',
            activebackground='#836fff',
            activeforeground='#1a1b2f',
            font=('Courier', 12),
            relief=FLAT,
            width=125
        )
        button_execute.pack(side=LEFT, padx=5)

        button_browse = tk.Button(
            buttons_frame,
            text=' Browse',
            command=self.load_file_txt,
            image=self.img_browser,
            compound=LEFT,
            bg='#6a5acd',
            fg='#dcdcdc',
            activebackground='#836fff',
            activeforeground='#1a1b2f',
            font=('Courier', 12),
            relief=FLAT,
            width=125
        )
        button_browse.pack(side=LEFT, padx=5)

        button_save = tk.Button(
            buttons_frame, text=' Save', command=self.save_csv,
            image=self.img_save_file,
            compound=LEFT,
            bg='#6a5acd', fg='#dcdcdc', activebackground='#836fff',
            activeforeground='#1a1b2f', font=('Courier', 12),
            relief=FLAT, width=125
        )
        button_save.pack(side=LEFT, padx=5)

        # Input Expr Frame
        input_frame = tk.Frame(self, bg='#1a1b2f')
        input_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Results frame
        output_frame = tk.Frame(self, bg='#1a1b2f')
        output_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(5, 10))
        output_frame.grid_rowconfigure(0, weight=1)
        output_frame.grid_columnconfigure(0, weight=2)
        output_frame.grid_columnconfigure(1, weight=5)
        output_frame.grid_propagate(True)

        self.content_input = scrolledtext.ScrolledText(
            input_frame, wrap=tk.WORD, bg='#2b2d4f', fg='#dcdcdc',
            insertbackground='#dcdcdc', font=('Courier', 12), borderwidth=0
        )
        self.content_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.result_output = scrolledtext.ScrolledText(
            output_frame, wrap=tk.WORD, state=tk.DISABLED, bg='#2b2d4f',
            fg='#dcdcdc', font=('Courier', 12), borderwidth=0
        )
        self.result_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def save_csv(self): # ahora guarda txt pero se mantendra el nombre anterior
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt")],
            title="Guardar archivo de texto"
        )

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    content = self.content_input.get("1.0", tk.END)
                    file.write(content)
            except Exception as e:
                self.display_result(f"Error saving file: {str(e)}", False)

    def load_file_txt(self):
        file_path = filedialog.askopenfilename(
            title="Selecciona un archivo .txt",
            filetypes=[("Archivos TXT", "*.txt")]
        )

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.content_input.delete('1.0', tk.END)
                self.content_input.insert(tk.END, content)
            except Exception as e:
                self.display_result(f"Error reading file: {str(e)}", False)

    def display_result(self, message, is_valid):
        self.result_output.config(state=tk.NORMAL)
        self.result_output.delete(1.0, tk.END)

        tag = "valid" if is_valid else "invalid"
        color = "#66ff66" if is_valid else "#ff6666"

        self.result_output.tag_configure(tag, foreground=color)
        self.result_output.insert(tk.END, message, tag)
        self.result_output.config(state=tk.DISABLED)

    def validate_text(self):
        input_text = self.content_input.get("1.0", tk.END)
        try:
            result = api_connection(input_text)
            print(result)
            self.display_result(result, True)
        except Exception as e:
            self.display_result(f"Error en el análisis: {str(e)}", False)
