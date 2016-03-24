import os
from os import remove, close, rename
from shutil import move
from os.path import isfile, join
from tempfile import mkstemp


def replace_app_template(path, project_name):
    for dirname in os.listdir(path):
        if isfile(join(path, dirname)):
            replace(join(path, dirname), "app_template", project_name)
        else:
            replace_app_template(join(path, dirname), project_name)
            if dirname == "app_template":
                rename(join(path, dirname), join(path, project_name))


def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)
