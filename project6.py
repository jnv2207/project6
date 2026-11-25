
import os
from datetime import datetime


class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # Create file using x mode
    def create_file(self):
        try:
            with open(self.filename, "x") as file:
                pass
        except FileExistsError:
            pass
        except PermissionError:
            print("Error: Permission denied.")

    # Add a new journal entry
    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry: ")

            if not entry.strip():
                print("Entry cannot be empty.")
                return

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n")
                file.write("-" * 40 + "\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied.")

        except OSError as error:
            print("File error:", error)

    # View all journal entries
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

            if content.strip():
                print("\nYour Journal Entries:")
                print("-" * 40)
                print(content)
            else:
                print("No journal entries found.")

        except FileNotFoundError:
            print("No journal file exists. Add an entry first.")

        except PermissionError:
            print("Error: Permission denied.")

        except OSError as error:
            print("File error:", error)

    # Search journal entries
    def search_entry(self):
        try:
            keyword = input(
                "\nEnter a keyword or date to search: "
            ).lower()

            with open(self.filename, "r") as file:
                entries = file.read().split("-" * 40)

            found = False

            print("\nMatching Entries:")

            for entry in entries:
                if keyword in entry.lower():
                    print(entry.strip())
                    print("-" * 40)
                    found = True

            if not found:
                print("No matching entries found.")

        except FileNotFoundError:
            print("The journal file does not exist.")

        except PermissionError:
            print("Error: Permission denied.")

        except OSError as error:
            print("File error:", error)

    # Delete all journal entries
    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("No journal entries to delete.")
                return

            confirmation = input(
                "Are you sure you want to delete all entries? "
                "(yes/no): "
            ).lower()

            if confirmation == "yes":
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            else:
                print("Deletion cancelled.")

        except PermissionError:
            print("Error: Permission denied.")

        except OSError as error:
            print("File error:", error)

    # Demonstrate w mode
    def demonstrate_write_mode(self):
        try:
            with open(self.filename, "w") as file:
                file.write("")

            print("File opened using write mode.")

        except PermissionError:
            print("Error: Permission denied.")

        except OSError as error:
            print("File error:", error)

    # Main menu
    def menu(self):
        self.create_file()

        while True:
            print("\n================================")
            print("   PERSONAL JOURNAL MANAGER")
            print("================================")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("\nPlease select an option: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                print(
                    "Thank you for using Personal Journal Manager."
                )
                print("Goodbye!")
                break

            else:
                print(
                    "Invalid option. Please select 1 to 5."
                )


# Create object and run program
if __name__ == "__main__":
    journal = JournalManager()
    journal.menu()
