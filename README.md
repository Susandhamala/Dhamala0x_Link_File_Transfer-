Dhamala0x_Link_File_Transfer-
Dhamala0x_Link_File_Transfer is a result of that motivation. It’s not just a project to showcase coding skills it’s a practical solution built from a real need for privacy.

Dhamala0x_Link_File_Transfer- - Encrypted File Transfer Tool by Susan Dhamala (0x4m4)
=====================================================================

Dhamala0x_Link_File_Transfer is a secure file transfer tool designed by Susan Dhamala (0x4m4). This tool ensures that your files are transferred safely and confidentially over the network using AES-256 encryption and a futuristic, user-friendly interface.

Features
AES-256 Encryption: Secures files using industry-standard advanced encryption.
PBKDF2 Key Derivation: Safeguards passwords with salt and 100,000 iterations.
Futuristic GUI: Styled with a dark theme and clean layout using Tkinter.
End-to-End File Protection: Files are encrypted before leaving your device.
File Integrity: Maintains original file name and structure.
Why Dhamala0x_Link_File_Transfer?
Unlike many public file sharing platforms, Dhamala0x_Link_File_Transfer ensures full privacy and integrity of data transfer. Encryption happens locally, so no one—not even your network—can peek inside the contents. This makes it ideal for ethical hackers, cybersecurity professionals, and privacy-focused users.

Works seamlessly on:

Windows
Linux
macOS
Android (via compatible Python environments)
Requirements
Python 3.x installed along with the following libraries:

tkinter
socket (built-in)
cryptography
Installation
Clone the repository:

https://github.com/Susandhamala/Dhamala0x_Link_File_Transfer
git clone https://github.com/0x4m4/ Dhamala0x_Link_File_Transfer.git
cd  Dhamala0x_Link_File_Transfer
Install required libraries:

pip install cryptography
pip install tkinter
Usage
Run the GUI:

python  Dhamala0x_Link_File_Transfer.py
Sending a File:

Launch Dhamala0x_Link_File_Transfer.
Select "Send" mode.
Enter the receiver's host IP and port.
Choose a file to send.
Enter a secure password.
Click "Execute" to encrypt and transmit the file.
Receiving a File:

Launch Dhamala0x_Link_File_Transfer.
Select "Receive" mode.
Enter the port to listen on.
Enter the password (must match sender's).
Click "Execute" to begin receiving and decrypting.
Example Usage
Send:

Mode: Send
Host: 192.168.1.100
Port: 12345
File: any_file.txt
Password: strongpassword
Execute
Receive:

Mode: Receive
Port: 12345
Password: strongpassword
Execute
Security
Dhamala0x_Link_File_Transfer incorporates advanced cryptographic standards:

AES-256: Military-grade file encryption
PBKDF2 with HMAC-SHA256: Hardened key generation
Random IV for every session: Prevents replay and pattern attacks
Screenshots
(Add screenshots here if applicable)

Error Handling & Prompts
The application will provide real-time guidance:

Missing Fields: Prompts you to fill host/port/password.
Invalid Inputs: Displays errors for bad port numbers or empty file paths.
Transfer Status: Informs you whether a file is sent/received successfully.
Decryption Failures: Alerts if the password is incorrect or data is corrupted.
Disclaimer
While Dhamala0x_Link_File_Transfer uses strong encryption techniques, your overall security depends on using a strong password and keeping it secret. Share passwords securely and avoid common or reused credentials.
