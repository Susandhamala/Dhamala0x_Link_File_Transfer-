Dhamala0x_Link_File_Transfer
A lightweight and secure peer-to-peer file transfer tool built using Python. It uses strong encryption and a user-friendly graphical interface for simple and safe file sharing between devices over LAN.

Features:

AES-256 encryption for secure file transmission

Password-based key derivation using PBKDF2

GUI for both sending and receiving files using Tkinter

Peer-to-peer, no need for third-party servers

Cross-platform: Works on both Windows and Linux

Requirements:

Python version 3.6 or higher

Libraries: tkinter, socket, cryptography

Use pip to install cryptography:
pip install cryptography

How to Use:

Sender Side:

Run the application by executing: python main.py

Click "Send File"

Enter the receiver’s IP address and port number

Enter a secure password

Choose the file to send

Click “Send File”

Receiver Side:

Run the application on the receiving machine

Click "Receive File"

Enter the host (0.0.0.0 recommended), port number, and the same password

Click “Start Receiving”

The received file will be saved with the original name

Testing Instructions:

To test the encryption module, run: python test_crypto.py

Tests include:

Key length check

Padding/unpadding verification

Encryption and decryption accuracy

Ensuring random encryption IVs for each session

Project Files:

main.py : Main application file

test_crypto.py : Contains unit tests

README.txt : Project documentation

Author:
Susan Dhamala (0xxProtocool)
Student ID: 240170 / 15381093
Softwarica College of IT & E-Commerce
Coventry University
Module: ST5068CEM – Programming and Algorithm
