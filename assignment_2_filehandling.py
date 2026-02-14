# -------------------- Question 1: Reading a File --------------------

def read_file():
    try:
        with open("sample.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

print("Question 1 Output:")
read_file()


# -------------------- Question 2: Writing to a File --------------------

def write_file(lines):
    with open("output.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")

print("\nQuestion 2 Output:")
write_file(["Line 1", "Line 2", "Line 3"])


# -------------------- Question 3: Copying a File --------------------

def copy_file():
    try:
        with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
            dest.write(src.read())
    except FileNotFoundError:
        print("Source file not found.")

print("\nQuestion 3 Output:")
copy_file()


# -------------------- Question 4: Appending to a File --------------------

def append_file(text):
    with open("log.txt", "a") as file:
        file.write(text + "\n")

print("\nQuestion 4 Output:")
append_file("New log entry")


# -------------------- Question 5: Counting Words in a File --------------------

def count_words():
    try:
        with open("document.txt", "r") as file:
            content = file.read()
            return len(content.split())
    except FileNotFoundError:
        print("File not found.")

print("\nQuestion 5 Output:", count_words())


# -------------------- Question 6: Finding and Replacing Text --------------------

def find_replace(old_word, new_word):
    try:
        with open("data.txt", "r") as file:
            content = file.read()
        content = content.replace(old_word, new_word)
        with open("data.txt", "w") as file:
            file.write(content)
    except FileNotFoundError:
        print("File not found.")

print("\nQuestion 6 Output:")
find_replace("old", "new")


# -------------------- Question 7: Reading a File in Reverse --------------------

def read_reverse():
    try:
        with open("reverse.txt", "r") as file:
            lines = file.readlines()
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

print("\nQuestion 7 Output:")
read_reverse()


# -------------------- Question 8: Counting Lines, Words, and Characters --------------------

def file_stats():
    try:
        with open("stats.txt", "r") as file:
            content = file.read()
            lines = content.splitlines()
            words = content.split()
            chars = len(content)
            return len(lines), len(words), chars
    except FileNotFoundError:
        print("File not found.")

print("\nQuestion 8 Output:", file_stats())


# -------------------- Question 9: Merging Multiple Files --------------------

def merge_files(file_list):
    with open("merged.txt", "w") as outfile:
        for fname in file_list:
            try:
                with open(fname, "r") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")
            except FileNotFoundError:
                print(f"{fname} not found.")

print("\nQuestion 9 Output:")
merge_files(["file1.txt", "file2.txt"])


# -------------------- Question 10: Splitting a Large File --------------------

def split_file():
    try:
        with open("large.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 100):
                with open(f"part_{i//100 + 1}.txt", "w") as part:
                    part.writelines(lines[i:i+100])
    except FileNotFoundError:
        print("File not found.")

print("\nQuestion 10 Output:")
split_file()


# -------------------- Question 11: Creating a Log File --------------------

from datetime import datetime

def create_log(message):
    with open("activity.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

print("\nQuestion 11 Output:")
create_log("Activity started")


# -------------------- Question 12: Binary File Operations --------------------

def copy_binary():
    try:
        with open("image.bin", "rb") as src, open("copy_image.bin", "wb") as dest:
            dest.write(src.read())
    except FileNotFoundError:
        print("Binary file not found.")

print("\nQuestion 12 Output:")
copy_binary()


# -------------------- Question 13: CSV File Operations --------------------

import csv

def read_csv_file():
    try:
        with open("data.csv", "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
            print(data)
    except FileNotFoundError:
        print("CSV file not found.")

print("\nQuestion 13 Output:")
read_csv_file()


# -------------------- Question 14: JSON File Operations --------------------

import json

def read_json_file():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        print("JSON file not found.")

print("\nQuestion 14 Output:")
read_json_file()


# -------------------- Question 15: File Permission Handling --------------------

def read_protected():
    try:
        with open("protected.txt", "r") as file:
            print(file.read())
    except PermissionError:
        print("Permission denied.")
    except FileNotFoundError:
        print("File not found.")

print("\nQuestion 15 Output:")
read_protected()
