import tkinter as tk
from tkinter import messagebox

def generate_keys():
    try:
        p = int(public_int_one.get("1.0", "end-1c"))
        g = int(public_int_two.get("1.0", "end-1c"))
        a = int(private_int_alice.get("1.0", "end-1c"))
        b = int(private_int_bob.get("1.0", "end-1c"))
        
        A = (g ** a) % p
        B = (g ** b) % p
        shared_secret_alice = (B ** a) % p
        shared_secret_bob = (A ** b) % p
        
        result_label.config(text=f"Alice's Public Key: {A}\nBob's Public Key: {B}\n"
                               f"Shared Secret (Alice): {shared_secret_alice}\n"
                               f"Shared Secret (Bob): {shared_secret_bob}")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input! Please enter valid integers.")

root = tk.Tk()
root.title("Diffie-Hellman Key Exchange")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Labels & Inputs
labels = ["Public Number 1 (P):", "Public Number 2 (G):", "Private Number for Alice:", "Private Number for Bob:"]
inputs = []

for i, text in enumerate(labels):
    tk.Label(root, text=text, font=("Arial", 12), bg="#f0f0f0").grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Text(root, height=1, width=15, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    inputs.append(entry)

public_int_one, public_int_two, private_int_alice, private_int_bob = inputs

# Generate Button
generate_button = tk.Button(root, text="Generate Keys", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=generate_keys)
generate_button.grid(row=4, column=0, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333", justify="center")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()