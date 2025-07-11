# Mail Merge Project with Python

This is a straightforward Mail Merge project developed in Python. I built it as part of the "100 Days of Python" challenge to practice file handling and basic text automation.

---

## What This Project Does

The program reads a list of names from one text file and a letter template from another. For each name, it generates a personalized letter by replacing a `[name]` placeholder in the template. All the personalized letters are then saved as individual text files in an output folder.

---

## What I Learned

During this project, I gained practical experience and solidified my understanding of several key Python concepts:

* **File Handling (`open()`):** How to open files for reading (`'r'`) and writing (`'w'`), and the importance of using `with open(...)` to ensure files are closed properly.
* **Reading File Content (`.read()`, `.readlines()`):** I learned the difference between reading an entire file's content as a single string (`.read()`) versus reading it line by line into a list (`.readlines()`).
* **String Manipulation (`.strip()`, `.replace()`):**
    * I used `.strip()` to remove unwanted characters (like newline characters `\n`) from the beginning and end of strings.
    * I applied `.replace()` to swap specific parts of the text (like the `[name]` placeholder) with dynamic content (the guest's name).
* **Project Structure:** I practiced organizing project files into a clear directory structure for better maintainability.

---