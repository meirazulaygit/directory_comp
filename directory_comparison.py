import os
import filecmp
import sys
from PIL import Image


def differences_report_between_two_dir(dir1_path, dir2_path):
    print(filecmp.dircmp(dir1_path, dir2_path).report())


def compare_image(image_path1, image_path2):
    with Image.open(image_path1) as pic1, Image.open(image_path2) as pic2:
        if pic1.tobytes() == pic2.tobytes():
            print(f"Image {image_path1} and {image_path2} are identical")


def compare_archives(archive_path1, archive_path2):
        if os.path.getsize(archive_path1) == os.path.getsize(archive_path2):
            print(f"archive {archive_path1} and {archive_path2} are identical")


def compare_two_directories(dir1_path, dir2_path):
    differences_between_dir1_to_dir2 = filecmp.dircmp(dir1_path, dir2_path)

    for file in  differences_between_dir1_to_dir2.common_files:
        file1 = os.path.join(dir1_path, file)
        file2 = os.path.join(dir2_path, file)

        if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            compare_image(file1, file2)

        elif file.endswith(('.zip', '.tar', '.etc')):
            compare_archives(file1, file2)


if __name__ == "__main__":
    dir1_path = 'tests/dir1'
    dir2_path = 'tests/dir2'
    differences_report_between_two_dir(dir1_path, dir2_path)
    compare_two_directories(dir1_path, dir2_path)

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python script.py path/to/dir1 path/to/dir2")
#         sys.exit(1)
#
#     dir1_path = sys.argv[1]
#     dir2_path = sys.argv[2]
#
#     differences_report_between_two_dir(dir1_path, dir2_path)
#     compare_two_directories(dir1_path, dir2_path)