import os
from datetime import datetime, timedelta
from tkinter import scrolledtext, filedialog
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from antlr4 import InputStream, CommonTokenStream
from backend.output.InvoiceLexer import InvoiceLexer
from backend.output.InvoiceParser import InvoiceParser
from backend.pdf_generator import generate_bill_pdf
from utils.classes.InvoiceCounter import invoice_counter
from backend.MyVisitor import MyVisitor


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
        self.bill_data = None

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
        self.img_genr_pdf = self.load_image("generate-pdf.png")

        buttons_frame = tk.Frame(self, bg='#1a1b2f')
        buttons_frame.grid(row=0, column=0, sticky="n", padx=10, pady=(10, 5))

        # Botón Analyze con imagen
        button_execute = tk.Button(
            buttons_frame,
            text=' Analyse',
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
            buttons_frame, text=' Save', command=self.save_file,
            image=self.img_save_file,
            compound=LEFT,
            bg='#6a5acd', fg='#dcdcdc', activebackground='#836fff',
            activeforeground='#1a1b2f', font=('Courier', 12),
            relief=FLAT, width=125
        )
        button_save.pack(side=LEFT, padx=5)

        button_generate = tk.Button(
            buttons_frame,
            text=' Generate Bill',
            command=self.generate_invoice,
            image=self.img_genr_pdf,
            compound=LEFT,
            bg='#6a5acd',
            fg='#dcdcdc',
            activebackground='#836fff',
            activeforeground='#1a1b2f',
            font=('Courier', 12),
            relief=FLAT,
            width=200
        )
        button_generate.pack(side=LEFT, padx=5)

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

    def save_file(self):  # ahora guarda txt pero se mantendra el nombre anterior
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
            input_stream = InputStream(input_text)
            lexer = InvoiceLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = InvoiceParser(token_stream)
            tree = parser.invoice()
            visitor = MyVisitor()

            # Obtener la factura generada
            self.bill_data = visitor.visit(tree)

            # Añadir campos adicionales y asegurar que no sean None
            self.bill_data.update({
                "empresa_nombre": "Frutas de la Barragang",
                "empresa_direccion": "Blvd. Tecnológico 150\nEx Ejido Chapultepec, CP 22780",
                "enviar_a": self.bill_data.get("facturar_a", ""),
                "numero_factura": invoice_counter.get_next(),
                "fecha_factura": datetime.now().strftime("%d/%m/%Y"),
                "numero_pedido": "PED-" + datetime.now().strftime("%Y%m%d"),
                "fecha_vencimiento": (datetime.now() + timedelta(days=15)).strftime("%d/%m/%Y"),
                "subtotal": self.bill_data.get("subtotal", 0),  # Usar 0 si no está presente
                "iva": round(self.bill_data.get("subtotal", 0) * 0.21, 2),  # Calcular IVA
                "total": round(self.bill_data.get("subtotal", 0) * 1.21, 2),  # Calcular total
                "condiciones": "Pago en 15 días\nCuenta: ES12 3456 7891\nBanco: Banco Ejemplo"
            })

            self.display_result("Bill validated", True)
        except Exception as e:
            self.display_result(f"Error en el análisis: {str(e)}", False)

    def generate_invoice(self):
        if not self.bill_data:
            self.display_result("Primero valida los datos con Analyze", False)
            return

        try:
            # Verificar campos requeridos
            required_fields = [
                'empresa_nombre', 'empresa_direccion', 'facturar_a', 'enviar_a',
                'numero_factura', 'fecha_factura', 'items', 'subtotal', 'iva', 'total'
            ]

            missing = [field for field in required_fields if field not in self.bill_data]
            if missing:
                raise ValueError(f"Faltan campos: {', '.join(missing)}")

            file_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                title="Guardar Factura como PDF"
            )

            if file_path:
                generate_bill_pdf(file_path, self.bill_data)
                self.display_result(f"PDF generado en:\n{file_path}", True)

        except Exception as e:
            self.display_result(f"Error al generar PDF: {str(e)}", False)