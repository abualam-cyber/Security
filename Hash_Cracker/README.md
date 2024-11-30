
# Hash Cracker Tool

This tool is a GUI application for brute-forcing hashes using MD5, SHA-1, or SHA-256 algorithms.

## Features
- Supports dictionary-based attacks (if implemented in the future).
- Brute-force attacks with a customizable character set and maximum length.
- Real-time progress tracking with the ability to stop operations.

## Usage
Run the `hash_cracker_gui.py` script:
```bash
python hash_cracker_gui.py
```

## Requirements
- Python 3.x
- tkinter

The Hash Cracker GUI application is a Python-based tool that attempts to crack hashes using a brute-force approach. It has a graphical user interface (GUI) for ease of use, allowing the user to enter the hash value, select a hashing algorithm, define the character set, and specify the maximum length of the password. The tool utilizes multithreading to maintain responsiveness while performing the brute-force attack.

#######################################################################################################################################
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
########################################################################################################################################
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
########################################################################################################################################
Using the GUI:

Enter the target hash value that you want to crack.

Select the hashing algorithm from the dropdown (md5, sha1, sha256).

Define the character set (e.g., abcdefghijklmnopqrstuvwxyz for lowercase letters).

Set the maximum length of the password to try.

Click Start to begin the brute-force process.

Monitor progress with the progress bar and use Stop to terminate the process if needed.
########################################################################################################################################
Notes

The brute-force approach can be very slow, especially with long maximum lengths or complex character sets.

This application is designed for educational purposes to demonstrate the vulnerability of weak hashes and the importance of strong passwords.
########################################################################################################################################
Disclaimer

Use this application responsibly. Hash cracking should only be performed on hashes that you own or have permission to crack.

