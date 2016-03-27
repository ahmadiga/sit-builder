import os
import re
from os import remove, close, rename
from os.path import isfile, join
from shutil import move
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


def add_app_to_settings(name, CURRENT_PATH):
    for dirname in os.listdir(CURRENT_PATH):
        if isfile(join(CURRENT_PATH, dirname)) and re.match('(settings.py)', dirname):
            my_file = open(CURRENT_PATH + '/' + name, "r")
            searchlines = my_file.readlines()
            my_file.close()
            index = searchlines.count()
            for i, line in enumerate(searchlines):
                if line.__contains__('INSTALLED_APPS += ['):
                    index = i + 1
                    break
            line_to_be_added = "   '" + name + "',"
            searchlines.insert(index, line_to_be_added)
            my_file = open(CURRENT_PATH + '/' + name, "w")
            my_file.writelines(searchlines)
            my_file.close()
            break
