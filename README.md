
**Dhamala0x\_Link\_File\_Transfer - Encrypted File Transfer Tool**
**By Susan Dhamala (0x4m4)**

---

**Overview**
Dhamala0x\_Link\_File\_Transfer is a secure, peer-to-peer encrypted file transfer utility developed by Susan Dhamala (alias: 0x4m4). This tool was born out of the necessity for private, encrypted communication over local networks and is designed with simplicity, security, and cross-platform support in mind.

It’s more than just a programming assignment—it's a real-world solution for secure file transmission in ethical hacking, cybersecurity training, and personal privacy scenarios.

---

**🔒 Key Features**

* **AES-256 Encryption:** Uses military-grade encryption to protect file content.
* **PBKDF2 Key Derivation:** Strengthens passwords using salt and 100,000 iterations.
* **Graphical Interface (GUI):** Built with Tkinter using a clean and futuristic dark theme.
* **Cross-Platform Compatibility:** Works on Windows, Linux, macOS, and even Android via compatible Python environments.
* **No External Servers:** All encryption and file processing is local; no data is stored or transmitted externally.

---

**🧑‍💻 Why Use This Tool?**
Unlike many cloud-based file transfer tools, Dhamala0x\_Link\_File\_Transfer ensures full **end-to-end confidentiality**. File encryption happens on the sender's device and decryption on the receiver's side using a shared password. Ideal for:

* Ethical Hackers
* Cybersecurity Professionals
* Students and Privacy Advocates

---

**💻 Requirements**

* **Python 3.x**
* **Libraries:**

  * tkinter
  * socket (standard)
  * cryptography

---

**📦 Installation**

1. **Clone the Repository**

```bash
git clone https://github.com/0x4m4/Dhamala0x_Link_File_Transfer.git
cd Dhamala0x_Link_File_Transfer
```

2. **Install Dependencies**

```bash
pip install cryptography
pip install tkinter  # Pre-installed in most systems with Python
```

---

**🚀 How to Use**

**To Send a File:**

1. Run the program:
   `python Dhamala0x_Link_File_Transfer.py`
2. Choose **"Send"**
3. Enter:

   * Recipient's IP address (e.g., 192.168.1.100)
   * Port (e.g., 12345)
   * Password (e.g., strongpassword)
   * Choose the file
4. Click **Execute** to encrypt and transmit

**To Receive a File:**

1. Run the program:
   `python Dhamala0x_Link_File_Transfer.py`
2. Choose **"Receive"**
3. Enter:

   * Listening Port (e.g., 12345)
   * Password (must match sender)
4. Click **Execute** to start listening and decrypting

---

**📂 Example**

**Sender Side:**

```
Mode: Send
Host: 192.168.1.100
Port: 12345
File: mydata.pdf
Password: strongpassword
Click: Execute
```

**Receiver Side:**

```
Mode: Receive
Port: 12345
Password: strongpassword
Click: Execute
```

---

**🛡️ Security**

* **AES-256-CBC:** Secure file encryption with a random IV
* **PBKDF2-HMAC-SHA256:** Prevents brute-force attacks on passwords
* **Random IV Per Session:** Prevents known-plaintext and replay attacks

---

**🖼️ Screenshots**


**⚠️ Error Handling & User Prompts**

* **Missing Fields:** Alerts for empty host, port, password, or file
* **Invalid Inputs:** Handles invalid port types and unreachable IPs
* **Transfer Status:** Shows “File Sent” or “File Received” confirmations
* **Decryption Errors:** Alerts if wrong password or corrupted file

---

**📢 Disclaimer**
Although Dhamala0x\_Link\_File\_Transfer uses strong cryptographic standards, **your security is only as strong as your password**. Always use complex, unique passwords and avoid sharing them over insecure channels.

