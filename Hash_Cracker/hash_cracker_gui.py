"""AUTHOR: ABU S. ALAM"""


"""Overview

The Hash Cracker GUI application is a Python-based tool that attempts to crack hashes using a brute-force approach. It has a graphical user interface (GUI) for ease of use, allowing the user to enter the hash value, select a hashing algorithm, define the character set, and specify the maximum length of the password. The tool utilizes multithreading to maintain responsiveness while performing the brute-force attack.

Main Components and Functions

1. HashCracker Class

This class is responsible for handling the core logic of hash cracking, including hashing strings and performing the brute-force operation.

__init__(self, target_hash, algorithm, charset, max_length)

Initializes the HashCracker instance with the given parameters.

Parameters:

target_hash (str): The hash value to be cracked.

algorithm (str): The hashing algorithm to use (e.g., md5, sha1, sha256).

charset (str): The character set to use for generating possible passwords.

max_length (int): The maximum length of the password to attempt.

Attributes:

stop_flag (bool): A flag to indicate when to stop the brute-force operation.

hash_string(self, input_string)

Computes the hash of the input string using the specified algorithm.

Parameters:

input_string (str): The string to be hashed.

Returns: The hashed value as a hexadecimal string.

Supported Algorithms: md5, sha1, sha256.

brute_force(self, progress_callback)

Attempts to crack the hash using a brute-force approach, generating all possible combinations of characters up to the specified maximum length.

Parameters:

progress_callback (function): A function to call to update the progress bar in the GUI.

Uses the itertools.product function to generate combinations from the given character set and tries hashing each combination to match the target hash.

2. Graphical User Interface (GUI)

The GUI is built using the tkinter library, and it allows users to input the necessary parameters for the hash cracking process.

Tk(): Creates the main window for the application.

Labels, Entry Widgets, and Buttons: These widgets allow the user to interact with the application:

Input Fields: The user can enter the target hash, select the hashing algorithm, define the character set, and specify the maximum length for the password.

Buttons:

Start Button: Begins the hash cracking process in a separate thread to prevent the GUI from freezing.

Stop Button: Stops the hash cracking process by setting the stop_flag.

Progressbar: Displays the progress of the brute-force operation.

Multithreading: Uses the threading library to run the brute-force cracking function in a separate thread, allowing the GUI to remain responsive.

How to Run the Application

Prerequisites

Python Version: Python 3.x

Dependencies: Install the required dependencies from requirements.txt.

Run the following command to install the dependencies:

pip install -r requirements.txt

Running the Application

Open a Terminal: Navigate to the directory containing the files.

Run the Python Script:

python hash_cracker_gui.py

Using the GUI:

Enter the target hash value that you want to crack.

Select the hashing algorithm from the dropdown (md5, sha1, sha256).

Define the character set (e.g., abcdefghijklmnopqrstuvwxyz for lowercase letters).

Set the maximum length of the password to try.

Click Start to begin the brute-force process.

Monitor progress with the progress bar and use Stop to terminate the process if needed.

Notes

The brute-force approach can be very slow, especially with long maximum lengths or complex character sets.

This application is designed for educational purposes to demonstrate the vulnerability of weak hashes and the importance of strong passwords.

Disclaimer

Use this application responsibly. Hash cracking should only be performed on hashes that you own or have permission to crack.

"""
import hashlib
import itertools
import string
from tkinter import Tk, Label, Entry, Button, filedialog
from tkinter.ttk import Progressbar
import threading

class HashCracker:
    def __init__(self, target_hash, algorithm, charset, max_length):
        self.target_hash = target_hash
        self.algorithm = algorithm
        self.charset = charset
        self.max_length = max_length
        self.stop_flag = False

    def hash_string(self, input_string):
        if self.algorithm == 'md5':
            return hashlib.md5(input_string.encode()).hexdigest()
        elif self.algorithm == 'sha1':
            return hashlib.sha1(input_string.encode()).hexdigest()
        elif self.algorithm == 'sha256':
            return hashlib.sha256(input_string.encode()).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {self.algorithm}")

    def brute_force(self, progress_callback):
        total_combinations = sum(len(self.charset) ** length for length in range(1, self.max_length + 1))
        tried_combinations = 0

        for length in range(1, self.max_length + 1):
            for combination in itertools.product(self.charset, repeat=length):
                if self.stop_flag:
                    return "Brute-force stopped."
                candidate = ''.join(combination)
                hashed_candidate = self.hash_string(candidate)
                tried_combinations += 1
                progress_callback(tried_combinations, total_combinations)

                if hashed_candidate == self.target_hash:
                    return f"Match found: {candidate}"

        return "No match found with brute-force."


class HashCrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Cracker")
        self.charset = string.ascii_letters + string.digits
        self.cracker = None

        Label(root, text="Hash Cracker Tool", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        Label(root, text="Enter Hash:").grid(row=1, column=0, sticky="e")
        self.hash_entry = Entry(root, width=40)
        self.hash_entry.grid(row=1, column=1, padx=5, pady=5)

        Label(root, text="Algorithm (md5, sha1, sha256):").grid(row=2, column=0, sticky="e")
        self.algorithm_entry = Entry(root, width=40)
        self.algorithm_entry.grid(row=2, column=1, padx=5, pady=5)

        Label(root, text="Max Length for Brute-Force:").grid(row=3, column=0, sticky="e")
        self.max_length_entry = Entry(root, width=40)
        self.max_length_entry.grid(row=3, column=1, padx=5, pady=5)

        self.progress_bar = Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=4, column=0, columnspan=2, pady=5)

        Button(root, text="Run Cracker", command=self.start_cracker).grid(row=5, column=0, pady=10)
        Button(root, text="Stop Cracker", command=self.stop_cracker).grid(row=5, column=1, pady=10)

        self.result_label = Label(root, text="", fg="green")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def update_progress(self, current, total):
        progress_percentage = int((current / total) * 100)
        self.progress_bar['value'] = progress_percentage
        self.root.update_idletasks()

    def start_cracker(self):
        target_hash = self.hash_entry.get()
        algorithm = self.algorithm_entry.get().lower()
        try:
            max_length = int(self.max_length_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid max length input.", fg="red")
            return

        self.result_label.config(text="Running...", fg="blue")
        self.progress_bar['value'] = 0
        self.cracker = HashCracker(target_hash, algorithm, self.charset, max_length)

        threading.Thread(target=self.run_brute_force).start()

    def run_brute_force(self):
        if self.cracker:
            result = self.cracker.brute_force(self.update_progress)
            self.result_label.config(text=result, fg="green" if "Match" in result else "red")

    def stop_cracker(self):
        if self.cracker:
            self.cracker.stop_flag = True
            self.result_label.config(text="Stopping...", fg="orange")


if __name__ == "__main__":
    root = Tk()
    app = HashCrackerApp(root)
    root.mainloop()
