#!/usr/bin/python

from filename_formatter import clean_str

import sys
import os
import shutil

def clean_dir(directory_path):
    new_directory_path = clean_str(directory_path)
    shutil.move(directory_path, new_directory_path)
    for root, dirs, files in os.walk(new_directory_path):
        for name in files:
            old_file_path = os.path.join(root, name)
            new_file_path = clean_str(old_file_path)
            shutil.move(old_file_path, new_file_path)
        for name in dirs:
            clean_dir(os.path.join(root, name))


clean_dir(sys.argv[1])
