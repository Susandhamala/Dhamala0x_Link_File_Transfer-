# Dhamala0x_Link_File_Transfer - Secure File Transfer Tool
# Author: Susan Dhamala (0xxProtocool)
# Developed for educational and secure communication purposes

import tkinter as tk
from tkinter import filedialog, messagebox
import socket
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import struct

# Key derivation function
def derive_key(password):
    salt = b'salt_'  # Static salt (Note: use random salt for production)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Padding helpers
def pad_data(data):
    padder = padding.PKCS7(128).padder()
    return padder.update(data) + padder.finalize()

def unpad_data(data):
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(data) + unpadder.finalize()

# Sender logic
def send_file(sock, filename, password):
    key = derive_key(password)
    with open(filename, 'rb') as file:
        file_data = pad_data(file.read())
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()
    filename_bytes = os.path.basename(filename).encode()
    sock.sendall(struct.pack('I', len(filename_bytes)) + filename_bytes)
    sock.sendall(iv + encrypted_data)

# Receiver logic
def decrypt_data(key, data):
    iv, encrypted_data = data[:16], data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return unpad_data(decryptor.update(encrypted_data) + decryptor.finalize())

def receive_file(key, host, port):
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver_socket.bind((host, port))
    receiver_socket.listen(1)
    print(f"Receiver is listening on {host}:{port}...")
    client_socket, addr = receiver_socket.accept()
    print("Connected with:", addr)

    filename_len = struct.unpack('I', client_socket.recv(4))[0]
    filename = client_socket.recv(filename_len).decode()
    encrypted_data = b""
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        encrypted_data += chunk

    try:
        with open(filename, 'wb') as f:
            f.write(decrypt_data(key, encrypted_data))
        messagebox.showinfo("Success", f"File received and saved as: {filename}")
    except ValueError as e:
        messagebox.showerror("Decryption Failed", str(e))

    client_socket.close()
    receiver_socket.close()

# Sender GUI
def launch_sender():
    win = tk.Toplevel()
    win.title("Send File - Dhamala0x_Link_File_Transfer")
    win.geometry('400x400')
    win.configure(bg='black')

    def choose_file():
        filename = filedialog.askopenfilename()
        file_label.config(text=filename)

    def send_action():
        host = host_entry.get()
        port = port_entry.get()
        password = pass_entry.get()
        filepath = file_label.cget("text")

        if not all([host, port, password, filepath]) or filepath == "No file chosen":
            messagebox.showwarning("Missing Fields", "Please fill in all fields and choose a file.")
            return

        try:
            port = int(port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            send_file(sock, filepath, password)
            sock.close()
            messagebox.showinfo("Success", "File sent successfully!")
        except Exception as e:
            messagebox.showerror("Send Failed", str(e))

    tk.Label(win, text="Recipient's Host:", bg='black', fg='white').pack(pady=5)
    host_entry = tk.Entry(win)
    host_entry.pack(pady=5)

    tk.Label(win, text="Recipient's Port:", bg='black', fg='white').pack(pady=5)
    port_entry = tk.Entry(win)
    port_entry.pack(pady=5)

    tk.Label(win, text="Encryption Password:", bg='black', fg='white').pack(pady=5)
    pass_entry = tk.Entry(win, show="*")
    pass_entry.pack(pady=5)

    file_label = tk.Label(win, text="No file chosen", bg='black', fg='white')
    file_label.pack(pady=5)

    tk.Button(win, text="Choose File", command=choose_file).pack(pady=5)
    tk.Button(win, text="Send File", command=send_action).pack(pady=10)

# Receiver GUI with Host & Port input
def launch_receiver():
    win = tk.Toplevel()
    win.title("Receive File - Dhamala0x_Link_File_Transfer")
    win.geometry('400x350')
    win.configure(bg='black')

    def receive_action():
        host = host_entry.get()
        port = port_entry.get()
        password = pass_entry.get()

        if not host or not port or not password:
            messagebox.showwarning("Missing Fields", "Please enter host, port, and password.")
            return

        try:
            port = int(port)
            receive_file(derive_key(password), host, port)
        except Exception as e:
            messagebox.showerror("Receive Failed", str(e))

    tk.Label(win, text="Host to Bind (e.g., 0.0.0.0):", bg='black', fg='white').pack(pady=5)
    host_entry = tk.Entry(win)
    host_entry.insert(0, "0.0.0.0")
    host_entry.pack(pady=5)

    tk.Label(win, text="Port to Listen On:", bg='black', fg='white').pack(pady=5)
    port_entry = tk.Entry(win)
    port_entry.pack(pady=5)

    tk.Label(win, text="Decryption Password:", bg='black', fg='white').pack(pady=5)
    pass_entry = tk.Entry(win, show="*")
    pass_entry.pack(pady=5)

    tk.Button(win, text="Start Receiving", command=receive_action).pack(pady=20)

# Main GUI
root = tk.Tk()
root.title("Dhamala0x_Link_File_Transfer - Secure File Tool")
root.geometry('400x250')
root.configure(bg='black')

tk.Label(root, text="Dhamala0x_Link_File_Transfer", font=('Helvetica', 16, 'bold'), fg='cyan', bg='black').pack(pady=10)
tk.Label(root, text="A Secure File Transfer Tool", fg='white', bg='black').pack(pady=5)

tk.Button(root, text="Send File", command=launch_sender).pack(pady=10)
tk.Button(root, text="Receive File", command=launch_receiver).pack(pady=10)

tk.Label(root, text="Created by Susan Dhamala (0xxProtocool)", font=('Helvetica', 8), fg='gray', bg='black').pack(side='bottom', pady=10)

root.mainloop()
