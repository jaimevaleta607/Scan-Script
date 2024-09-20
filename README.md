**Duplicate File Finder
**
This script scans a specified directory and finds duplicate files based on their content by comparing file hashes.

**How to Use**

**Run the script**

Open a terminal and run the following command:


python3 find_duplicates.py

**Enter the root directory**

When prompted, enter the path of the directory you want to scan for duplicates. Example:


Enter the root directory to search for duplicates: /Users/xxxxx/Downloads

**Check results**

The script will scan the directory and generate a list of duplicate files. The results, including both the duplicate and original file paths, will be saved to duplicates_output.txt in the script's directory.

**Example Output**

If duplicate files are found, the script will output something like this:


**Duplicate files found:**

Duplicate: /Users/xxxxx/Downloads/file1.txt
Original: /Users/jaimevaleta/Documents/file1.txt
If no duplicates are found:


No duplicate files found. Results written to duplicates_output.txt
