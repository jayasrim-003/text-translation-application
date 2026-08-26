import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root = tk.Tk()

root.title("Text Translation Application")
root.geometry("700x700")

translator = Translator()

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    selected_language = language_dropdown.get()

    if not text:
        messagebox.showwarning(
            "Input Required",
            "Please enter text to translate."
        )
        return

    if not selected_language:
        messagebox.showwarning(
            "Language Required",
            "Please select a target language."
        )
        return

    target_language = next(
        code for code, name in LANGUAGES.items()
        if name == selected_language
    )

    try:
        result = translator.translate(
            text,
            dest=target_language
        )

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.text)

    except Exception as error:
        messagebox.showerror(
            "Translation Error",
            "Unable to translate the text. Please check your internet connection and try again."
        )


def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    language_dropdown.set("")


input_label = ttk.Label(
    root,
    text="Enter text to translate:"
)
input_label.pack(pady=10)

input_text = tk.Text(
    root,
    height=8,
    width=70
)
input_text.pack(pady=10)

language_label = ttk.Label(
    root,
    text="Select target language:"
)
language_label.pack(pady=5)

language_options = list(LANGUAGES.values())

language_dropdown = ttk.Combobox(
    root,
    values=language_options,
    state="readonly",
    width=30
)
language_dropdown.pack(pady=5)
language_dropdown.set("english")

output_label = ttk.Label(
    root,
    text="Translated text:"
)
output_label.pack(pady=10)

output_text = tk.Text(
    root,
    height=8,
    width=70
)
output_text.pack(pady=10)

translate_button = ttk.Button(
    root,
    text="Translate",
    command=translate_text
)
translate_button.pack(pady=10)

clear_button = ttk.Button(
    root,
    text="Clear",
    command=clear_text
)
clear_button.pack(pady=5)

root.mainloop()