# project6

<img width="2400" height="640" alt="image" src="https://github.com/user-attachments/assets/5c94bf46-a152-4736-979e-8f5a9c3346fb" />

✨ Your thoughts. Your terminal. Your timeline. ✨
</div>

>
## 📖 About the Project

Personal Journal Manager is a menu-driven Python application that lets you keep a private journal right from your terminal. Every entry is timestamped and saved to a plain text file, and the whole program is built around a single, clean JournalManager class, which shows how OOP, file handling and exception handling work together.

💡 No crashes, no confusing tracebacks, just friendly messages that tell you what went wrong and what to do next.

.

## 🌟 Features

1️⃣	Add a New Entry : Appends a timestamped entry. Creates journal.txt automatically if it doesn't exist.

2️⃣	View All Entries: Prints every entry. Handles a missing file gracefully.

3️⃣	Search for an Entry : 	Finds entries by keyword or date	

4️⃣	Delete All Entries :	Deletes the journal, but only after a yes/no confirmation.

5️⃣	Exit :	Leaves the program with a friendly goodbye.


 ## 🖥️ Preview

<img width="1800" height="1040" alt="image" src="https://github.com/user-attachments/assets/11d82caa-b747-4a81-be43-39cccc629e6a" />




 
## 🚀 Getting Started
Prerequisites
Python 3.8 or newer (download)
No external libraries needed. Only the standard library is used (datetime, os).
Run it
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git

# 2. Move into the project folder
cd <your-repo-name>

# 3. Start the app
python journal_manager.py

## 🎮 How to Use

Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

<details> <summary><b>➕ 1 · Add a New Entry</b></summary>

Enter your journal entry:
Today was a productive day. I learned about file handling.

Entry added successfully!

</details> <details> <summary><b>📚 2 · View All Entries</b></summary>

Your Journal Entries:
----------------------------------
[2024-12-25 10:00:00]
Today was a productive day. I learned about file handling.

[2024-12-24 18:00:00]
Had a great session on OOP concepts!

## If the file doesn't exist:

No journal entries found. Start by adding a new entry.

</details> <details> <summary><b>🔍 3 · Search for an Entry</b></summary>

Enter a keyword or date to search: productive

Matching Entries:
----------------------------------
[2024-12-25 10:00:00]
Today was a productive day. I learned about file handling.

## No match:

No entries were found for the keyword: productive.

</details> <details> <summary><b>🗑️ 4 · Delete All Entries</b></summary>
  
Are you sure you want to delete all entries? (yes/no): yes
All journal entries have been deleted.

## If there is nothing to delete:

text
No journal entries to delete.
</details> <details> <summary><b>⚠️ Error handling and invalid input</b></summary>

Error: The journal file does not exist. Please add a new entry first.
Invalid option. Please select a valid option from the menu.

</details>



## 🏗️ Architecture

<img width="1920" height="880" alt="image" src="https://github.com/user-attachments/assets/feec0db9-3cb5-41b0-9ec7-96d3f6f3c3a4" />






## 🧱 OOP concepts used
1) Class & Object : JournalManager is instantiated once in main()
2) Encapsulation :	File name, file operations and error handling all live inside the class
3) Instance methods :	add_entry(), view_entries(), search_entries(), delete_entries()
4) Abstraction:	The menu only calls methods and never touches the file directly


## 📂 File Handling Modes
Mode	|                   Meaning                      |	Where it's used
r	    |       Read an existing file (error if missing) |	Viewing and searching entries
w     |	Write, and overwrite existing content          |	Explained here for comparison. Not used, because it would erase old entries
a	    | Append to the end, creating the file if needed |	Adding a new entry
x	    |Create a new file, error if it already exists	 |Safely creating journal.txt the first time


## 🛡️ Exception Handling
Exception	          |             When it happens                        |	What the user sees
FileNotFoundError	  |Viewing, searching or deleting with no journal file | 	A clear message asking them to add an entry first
PermissionError     |	The file is read-only or locked                    |	A message saying the file can't be accessed
ValueError          |The menu choice isn't a number from 1 to 5	.      | Please select a valid option from the menu."
OSError             | Any other file problem                            |	A generic, friendly error, so the program never crashes


## 📁 Project Structure
📦 personal-journal-manager
 ┣ 📂 assets
 ┃ ┣ 🖼️ banner.svg
 ┃ ┣ 🖼️ terminal-preview.svg
 ┃ ┗ 🖼️ architecture.svg
 ┣ 📜 journal_manager.py   ← main program (JournalManager class + menu)
 ┣ 📄 journal.txt          ← created automatically on first entry
 ┗ 📘 README.md

 ## 📝 Assumptions

The assignment asks for assumptions to be documented, so here they are:

Entry format: each entry is saved as [YYYY-MM-DD HH:MM:SS] on one line, followed by the text on the next line, and a blank line between entries.
Search: it is case-insensitive and checks both the timestamp line and the entry text, so searching 2024-12-25 (date) or productive (keyword) both work.
Multi-line entries: an entry is the single line the user types before pressing Enter.
Empty input: blank entries are rejected with a helpful message and are not saved.
Confirmation: only yes (any letter case) confirms deletion. Anything else cancels it.
Location: journal.txt is stored in the same folder the program is run from.
Text files only: the program works only with .txt files, as required.

## 🎯 Learning Objectives Covered

[x] File handling operations (read, write, append and more)
[x] File opening modes r, w, a, x and their impact
[x] I/O operations (reading from and writing to files)
[x] Exceptions such as FileNotFoundError and PermissionError
[x] OOP principles to structure the application

## 👩‍💻 Author

Tejani Janvi B.Tech Computer Science Engineering ·

<div align="center">
⭐ If you like this project, give it a star! ⭐

Made with 💜 and Python

</div>

   







