# Directory_Comparison

This Python script allows you to compare two directories, identifying differences in files, including images and archives.

Introduction
The script compares two directories (dir1 and dir2) and reports the differences in files between them.
It performs specific checks for images and archives, utilizing the Pillow library for image comparison.

Requirements
Python 3.x
Pillow library (pip install Pillow)
Usage
Clone the repository: git clone [https://github.com/meirazulaygit/Directory_Comparsion.git](https://github.com/meirazulaygit/directory_comp.git)
Navigate to the script directory: cd /directory_comp
Script Details
differences_report_between_two_dir: Prints a report showing differences between two directories using the filecmp library.
compare_image: Compares images using the Pillow library.
compare_archives: Compares archive files based on their sizes.
compare_two_directories: Compares common files in two directories, performing specific checks for images and archives.
Sample Directories
The script is designed to work with sample directories (dir1 and dir2). Ensure these directories contain various file types,
including images (jpg, jpeg, png, gif) and archives (zip, tar, etc) for comprehensive testing.
