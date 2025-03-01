from tkinter import scrolledtext
from tkinter import *
import tkinter as tk
from libs.src.utils.classes.App import App
from antlr4 import ParseTreeWalker
from practicas2.csv.backend.csv_processing import csv_processing
from practicas2.csv.utils.classes.CSVValidation import CSVValidationListener


class GuiTerminal(App):
    def __init__(self, *args):
        super().__init__(*args)
        self.content_input = None
        self.result_output = None
        self.configure(bg='#1a1b2f')
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.current_scale = 1.0

        self.create_widgets()

    def create_widgets(self):
        buttons_frame = tk.Frame(self, bg='#1a1b2f')
        buttons_frame.grid(row=0, column=0, sticky="n", padx=10, pady=(10, 5))

        button_execute = tk.Button(
            buttons_frame, text='Analyse', command=self.validate_csv,
            bg='#6a5acd', fg='#dcdcdc', activebackground='#836fff',
            activeforeground='#1a1b2f', font=('Courier', 12),
            relief=FLAT, width=12
        )
        button_execute.pack(side=LEFT, padx=5)

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

        try:
            parser, lexer, tokens, error_handler = csv_processing(input_text)
            tree = parser.file_()
            listener = CSVValidationListener()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            all_errors = error_handler.errors + listener.errors

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

                success_msg = f"✅ Valid CSV\n{stats_info}"
                self.display_result(success_msg, is_valid=True)

        except Exception as e:
            self.display_result(f"Critic Error: {str(e)}", False)
