
# Directory Comparison 📂🔍

This Python script compares two directories, identifying differences in files, including images and archives.

## Requirements
- Python 3.x
- Pillow library (`pip install Pillow`)

## Usage
```bash
git clone https://github.com/meirazulaygit/Directory_Comparison.git
cd Directory_Comparison
```

## Script Details
- `differences_report_between_two_dir`: Prints differences using filecmp.
- `compare_image`: Compares images with Pillow.
- `compare_archives`: Compares archives based on sizes.
- `compare_two_directories`: Compares common files, checking for images and archives.

## Sample Directories
The script works with sample directories (`dir1` and `dir2`) with various file types for testing (jpg, jpeg, png, gif, zip, tar, etc).
