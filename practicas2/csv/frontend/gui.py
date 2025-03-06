import os
from tkinter import scrolledtext, filedialog, messagebox
from tkinter import *
import tkinter as tk
import csv
from PIL import Image, ImageTk
from antlr4 import ParseTreeWalker
from practicas2.csv.backend.csv_processing import csv_processing
from practicas2.csv.utils.classes.CSVValidation import CSVValidationListener
from practicas2.csv.backend.MyVisitor import MyVisitor


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

    def create_widgets(self):
        file_path = os.path.dirname(os.path.realpath(__file__))

        # Imagen para Browse
        img_browse_path = os.path.join(file_path, "folder-browser.png")
        if os.path.exists(img_browse_path):
            img_browse_file = Image.open(img_browse_path)
            img_browse_file = img_browse_file.resize((20, 20), Image.Resampling.LANCZOS)
            self.img_browser = ImageTk.PhotoImage(img_browse_file)
        else:
            self.img_browser = None

        # Imagen para Analyze
        img_analyse_path = os.path.join(file_path, "analyse-file.png")
        if os.path.exists(img_analyse_path):
            img_analyse_file = Image.open(img_analyse_path)
            img_analyse_file = img_analyse_file.resize((20, 20), Image.Resampling.LANCZOS)
            self.img_analyse = ImageTk.PhotoImage(img_analyse_file)
        else:
            self.img_analyse = None

        buttons_frame = tk.Frame(self, bg='#1a1b2f')
        buttons_frame.grid(row=0, column=0, sticky="n", padx=10, pady=(10, 5))

        # Botón Analyze con imagen
        button_execute = tk.Button(
            buttons_frame,
            text=' Analyse',
            command=self.validate_csv,
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
            command=self.load_csv,
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
            buttons_frame, text='Save', command=self.save_csv,
            bg='#6a5acd', fg='#dcdcdc', activebackground='#836fff',
            activeforeground='#1a1b2f', font=('Courier', 12),
            relief=FLAT, width=12
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


    def save_csv(self):
        input_text = self.content_input.get("1.0", tk.END).strip()  # Obtener el texto del CSV

        if not input_text:  # Verificar si el área de texto está vacía
            messagebox.showerror("Error", "No hay contenido para guardar.")
            return


        is_valid = self.validate_csv()
        if is_valid:
            pass


    def load_csv(self):
        file_path = filedialog.askopenfilename(
            title="Selecciona un archivo CSV",
            filetypes=[("Archivos CSV", "*.csv")]
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

    def validate_csv(self):
        input_text = self.content_input.get("1.0", tk.END)

        if not input_text.strip():
            self.display_result("✗ Invalid CSV: \nEmpty CSV", False)
            return

        if not input_text.strip() and self.csv_data is not None:
            input_text = self.csv_data.to_csv(index=False)

        try:
            parser, lexer, tokens, error_handler = csv_processing(input_text)
            tree = parser.file_()
            listener = CSVValidationListener()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            all_errors = error_handler.errors + listener.errors
            visitor = MyVisitor()
            visitor.visit(tree)

            if all_errors:
                self.display_result("✗ Invalid CSV", False)
                # self.display_result("\n".join(all_errors), False)
            else:
                stats_info = (
                    "\n\n"
                    "╒═══════════════════════════╕\n"
                    "│        STATISTICS         │\n"
                    "╞══════════════╤════════════╡\n"
                    "│ Fields/row   │ {:^10} │\n"
                    "├──────────────┼────────────┤\n"
                    "│ Total fields │ {:^10} │\n"
                    "╘══════════════╧════════════╛"
                ).format(
                    listener.num_fields_current_row,
                    listener.total_fields
                )

                header = visitor.headers
                rows = visitor.filas
                csv_name = "utils/docs/alumns.csv"
                with open(csv_name, mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(rows)

                csv_generated = f"\nCSV is located in {csv_name}"
                success_msg = f"✅ Valid CSV\n{stats_info}\n{csv_generated}"
                self.display_result(success_msg, is_valid=True)

        except Exception as e:
            self.display_result(f"Critical Error: {str(e)}", False)
