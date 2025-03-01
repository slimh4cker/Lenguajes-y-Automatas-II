from tkinter import scrolledtext
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from libs.src.utils.classes.App import App
from practicas2.expr_simplified.controller.code_execution import execute_code, generate_trees


class GuiTerminal(App):
    def __init__(self, *args):
        super().__init__(*args)
        self.tree_output = None
        self.configure(bg='#1a1b2f')
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.original_images = []
        self.tree_labels = []
        self.current_scale = 1.0
        self.tree_canvas = None
        self.scrollable_tree_frame = None
        self.tree_output = None

        self.create_widgets()

    def create_widgets(self):
        buttons_frame = tk.Frame(self, bg='#1a1b2f')
        buttons_frame.grid(row=0, column=0, sticky="n", padx=10, pady=(10, 5))

        # Botón Execute
        button_execute = tk.Button(
            buttons_frame, text='Execute', command=self.read_expr,
            bg='#6a5acd', fg='#dcdcdc', activebackground='#836fff',
            activeforeground='#1a1b2f', font=('Courier', 12),
            relief=FLAT, width=12
        )
        button_execute.pack(side=LEFT, padx=5)

        # Botón Show Tree
        button_tree = tk.Button(
            buttons_frame, text='Show Tree', command=self.show_trees,
            bg='#6a5acd', fg='#dcdcdc', activebackground='#836fff',
            activeforeground='#1a1b2f', font=('Courier', 12),
            relief=FLAT, width=12
        )
        button_tree.pack(side=LEFT, padx=5)

        button_clear = tk.Button(
            buttons_frame, text='Clear', command=self.clear_all,
            bg='#6a5acd', fg='#dcdcdc', activebackground='#836fff', activeforeground='#1a1b2f',
            font=('Courier', 12), relief=FLAT, width=12
        )
        button_clear.pack(side=LEFT, padx=5)

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

        arithmetic_output = tk.Frame(output_frame, bg='#2b2d4f')
        arithmetic_output.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        arithmetic_output.grid_rowconfigure(0, weight=1)
        arithmetic_output.grid_columnconfigure(0, weight=1)

        self.tree_output = tk.Frame(output_frame, bg='#2b2d4f')
        self.tree_output.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.tree_output.grid_rowconfigure(0, weight=1)
        self.tree_output.grid_columnconfigure(0, weight=1)

        self.tree_canvas = tk.Canvas(self.tree_output, bg='#2b2d4f', highlightthickness=0)
        scrollbar = tk.Scrollbar(self.tree_output, orient="vertical", command=self.tree_canvas.yview)
        self.scrollable_tree_frame = tk.Frame(self.tree_canvas, bg='#2b2d4f')

        self.scrollable_tree_frame.bind(
            "<Configure>",
            lambda e: self.tree_canvas.configure(
                scrollregion=self.tree_canvas.bbox("all")
            )
        )

        self.tree_canvas.create_window((0, 0), window=self.scrollable_tree_frame, anchor="nw")
        self.tree_canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tree_canvas.pack(side="left", fill="both", expand=True)

        self.expr_input = scrolledtext.ScrolledText(
            input_frame, wrap=tk.WORD, bg='#2b2d4f', fg='#dcdcdc',
            insertbackground='#dcdcdc', font=('Courier', 12), borderwidth=0
        )
        self.expr_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self.result_output = scrolledtext.ScrolledText(
            arithmetic_output, wrap=tk.WORD, state=tk.DISABLED, bg='#2b2d4f',
            fg='#dcdcdc', font=('Courier', 12), borderwidth=0
        )
        self.result_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

    def read_expr(self):
        input_expr = self.expr_input.get("1.0", tk.END).strip()
        lines = input_expr.split("\n")
        results = []

        for line in lines:
            if line.strip():
                result = execute_code(line.strip())
                results.append(result)

        self.update_results("\n".join(results))

    def show_trees(self):
        input_expr = self.expr_input.get("1.0", tk.END).strip()
        if not input_expr:
            return
        self.original_images = []
        image_buffers = generate_trees(input_expr)
        for buffer in image_buffers:
            self.original_images.append(Image.open(buffer))
        self.resize_trees()

    def delete_prev_trees(self):
        for widget in self.scrollable_tree_frame.winfo_children():
            widget.destroy()

    def add_separator(self, panel_width):
        separator = tk.Frame(self.scrollable_tree_frame,
                             height=2,
                             bg='#6a5acd',
                             width=panel_width)
        separator.pack(pady=5)

    def resize_trees(self):
        self.delete_prev_trees()
        self.tree_labels = []
        panel_width = self.tree_output.winfo_width() - 50
        for i, img in enumerate(self.original_images):
            aspect_ratio = img.width / img.height
            available_height = self.tree_output.winfo_height() - 20
            scaled_width = min(panel_width, available_height * aspect_ratio)
            scale_factor = scaled_width / img.width
            base_width = img.width
            scaled_width = int(base_width * scale_factor * self.current_scale)
            scaled_height = int(img.height * scale_factor * self.current_scale)
            resized_img = img.resize((scaled_width, scaled_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(resized_img)
            label = tk.Label(self.scrollable_tree_frame, image=photo, bg='#2b2d4f', borderwidth=0)
            label.photo = photo
            label.pack(pady=10, anchor="n")
            self.tree_labels.append(label)
            if i < len(self.original_images) - 1:
                self.add_separator(panel_width)

        self.tree_canvas.configure(scrollregion=self.tree_canvas.bbox("all"))

    def clear_all(self):
        self.expr_input.delete("1.0", tk.END)
        self.result_output.configure(state=tk.NORMAL)
        self.result_output.delete("1.0", tk.END)
        self.result_output.configure(state=tk.DISABLED)
        self.delete_prev_trees()
        self.tree_canvas.configure(scrollregion=(0, 0, 0, 0))
        self.original_images = []
        self.current_scale = 1.0
        self.update_idletasks()

    def update_results(self, results):
        self.result_output.configure(state=tk.NORMAL)
        self.result_output.delete("1.0", tk.END)
        self.result_output.insert(tk.END, results)
        self.result_output.configure(state=tk.DISABLED)
