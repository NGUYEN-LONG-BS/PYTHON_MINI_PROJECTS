import tkinter as tk
from tkinter import filedialog, messagebox
import json
from cryptography.fernet import Fernet
import os
from app.utils import *

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Config Encryption")
        self.border_width = 0
        
        entries_frame = tk.Frame(root, bd=self.border_width, relief="solid")
        entries_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
        
        self.entries = {}
        labels = ["DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD"]
        
        for i, label in enumerate(labels):
            tk.Label(entries_frame, text=label).grid(row=i, column=0, padx=10, pady=5, sticky='w')
            entry = tk.Entry(entries_frame, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label] = entry
        
        create_new_encrytion_files_button_frame = tk.Frame(root, bd=self.border_width, relief="solid")
        create_new_encrytion_files_button_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
        
        tk.Label(create_new_encrytion_files_button_frame, text="Tạo file key và encryt:", font=("Arial", 12), bg="#f0f0f5", anchor="w").grid(row=0, column=0, padx=5, pady=(5,0), sticky="w")
        tk.Button(create_new_encrytion_files_button_frame, text="Step-1: Generate Key", command=self.generate_key).grid(row=1, column=0, padx=5, pady=(5,0), sticky="w")
        tk.Button(create_new_encrytion_files_button_frame, text="Step-2: Encrypt & Save", command=self.encrypt_and_save).grid(row=2, column=0, padx=5, pady=(5,0), sticky="w")
        self.path_encryted_key = tk.Label(create_new_encrytion_files_button_frame, text="path key:", font=("Arial", 12), bg="#f0f0f5", anchor="w")
        self.path_encryted_key.grid(row=3, column=0, padx=5, pady=(5,0), sticky="w")
        self.path_encryted_json = tk.Label(create_new_encrytion_files_button_frame, text="path json:", font=("Arial", 12), bg="#f0f0f5", anchor="w")
        self.path_encryted_json.grid(row=4, column=0, padx=5, pady=(5,5), sticky="w")
        
        decryt_files_button_frame = tk.Frame(root, bd=self.border_width, relief="solid")
        decryt_files_button_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
        
        tk.Label(decryt_files_button_frame, text="Mã hoá file key và decrypt:", font=("Arial", 12), bg="#f0f0f5", anchor="w").grid(row=0, column=0, padx=5, pady=(5,0), sticky="w")
        tk.Button(decryt_files_button_frame, text="Step-3: Decrypt & Load", command=self.decrypt_and_load).grid(row=1, column=0, padx=5, pady=(5,5), sticky="w")
        
        information_frame = tk.Frame(root, bd=self.border_width, relief="solid")
        information_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")
        
        tk.Label(information_frame, text="Thông tin gợi ý theo cấu trúc sau:").grid(row=0, column=0, padx=5, pady=(5,0), sticky="ew")
        tk.Label(information_frame, text="DB_HOST: 123.123.123.123").grid(row=1, column=0, padx=5, pady=(5,0), sticky="w")
        tk.Label(information_frame, text="DB_NAME: TB_2024").grid(row=1, column=0, padx=5, pady=(5,0), sticky="w")
        tk.Label(information_frame, text="DB_USER: sa").grid(row=2, column=0, padx=5, pady=(5,0), sticky="w")
        tk.Label(information_frame, text="DB_PASSWORD: Ta###########").grid(row=3, column=0, padx=5, pady=(5,5), sticky="w")
        
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)
    
    def generate_key(self):
        key = Fernet.generate_key()
        os.makedirs(os.path.dirname(PATH_CONFIG_KEY), exist_ok=True)
        
        with open(PATH_CONFIG_KEY, "wb") as key_file:
            key_file.write(key)

        self.root.focus_force()
        self.path_encryted_key.config(text=f"path: {PATH_CONFIG_KEY}")
    
    def encrypt_and_save(self):
        # print("path key: ", self.path_key)
        if not os.path.exists(PATH_CONFIG_KEY):
            messagebox.showerror("Error", "Encryption key not found! Generate it first.")
            return
        
        with open(PATH_CONFIG_KEY, "rb") as key_file:
            encryption_key = key_file.read()
        cipher_suite = Fernet(encryption_key)
        
        config_data = {key: cipher_suite.encrypt(value.get().encode()).decode() for key, value in self.entries.items()}
        
        os.makedirs(os.path.dirname(PATH_CONFIG_JSON), exist_ok=True)
        with open(PATH_CONFIG_JSON, "w") as config_file:
            json.dump(config_data, config_file, indent=4)
        
        # Clear all entries
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        
        self.root.focus_force()
        self.path_encryted_json.config(text=f"path: {PATH_CONFIG_JSON}")
    
    def decrypt_and_load(self):
        messagebox.showinfo("Hướng dẫn", "Chọn đường dẫn đến file config.json")
        config_path = filedialog.askopenfilename(title="Select Config File", filetypes=[("JSON files", "*.json")])
        messagebox.showinfo("Hướng dẫn","Chọn đường dẫn đến file .key")
        key_path = filedialog.askopenfilename(title="Select Encryption Key", filetypes=[("Key files", "*.key")])
        
        if not config_path or not key_path:
            messagebox.showerror("Error", "Both config and key files must be selected.")
            return
        
        with open(key_path, "rb") as key_file:
            encryption_key = key_file.read()
        cipher_suite = Fernet(encryption_key)
        
        with open(config_path, "r") as config_file:
            encrypted_config = json.load(config_file)
        
        decrypted_config = {key: cipher_suite.decrypt(value.encode()).decode() for key, value in encrypted_config.items()}
        
        for key, value in decrypted_config.items():
            if key in self.entries:
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, value)
        
        messagebox.showinfo("Success", "Configuration successfully decrypted and loaded.")
        self.root.focus_force()

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
