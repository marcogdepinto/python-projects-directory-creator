"""
Create custom directories for Python projects.
The directory will include:
- A main.py script
- A README.md file
- A LICENSE file
- A requirements.txt file
"""

import os
import pathlib
import argparse


class MakeDirectory:
    """
    This is the main class of the application
    """
    def __init__(self,
                 directory_path,
                 script_file,
                 readme_file,
                 license_file,
                 requirements_file,
                 gitignore_file):

        self.directory_path = directory_path
        self.script_file = script_file
        self.readme_file = readme_file
        self.license_file = license_file
        self.requirements_file = requirements_file
        self.gitignore_file = gitignore_file

    def make_directory(self):
        """
        Constructor to create the directory
        """
        if not os.path.exists(self.directory_path):
            os.mkdir(self.directory_path)
            print("Directory", self.directory_path, "created ")
        else:
            print("Directory ", self.directory_path, " already exists")

    def make_file(self, which_file):
        """
        Constructor to create a file. Can be reused to create
        LICENSE, README and requirements.txt
        """

        file_path = os.path.join(pathlib.Path().absolute(), self.directory_path, which_file)
        try:
            if os.path.isfile(file_path):
                print("File " + which_file + " already exists")
            else:
                with open(file_path, 'w') as output_file:
                    output_file.write("# My " + which_file)
                print("File " + which_file + " created")
        except IOError as exception:
            raise IOError("%s: %s" % (file_path, exception.strerror))


if __name__ == '__main__':
    print("Starting execution..")
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--directory_path",
                        help="Folder name in which your project will be saved",
                        default="MyProject")
    PARSER.add_argument("--script_file",
                        help="Name of your script file. Default=main.py",
                        default="main.py")
    PARSER.add_argument("--readme_file",
                        help="Name of your README. Default=README.md",
                        default="README.md")
    PARSER.add_argument("--license_file",
                        help="Name of your LICENSE file. Default=LICENSE",
                        default="LICENSE")
    PARSER.add_argument("--requirements_file",
                        help="Name of your requirements file. Default=requirements.txt",
                        default="requirements.txt")
    PARSER.add_argument("--gitignore_file",
                        help="Name of your gitignore file. Default=.gitignore",
                        default=".gitignore")
    ARGS = PARSER.parse_args()
    LAUNCHER = MakeDirectory(ARGS.directory_path,
                             ARGS.script_file,
                             ARGS.readme_file,
                             ARGS.license_file,
                             ARGS.requirements_file,
                             ARGS.gitignore_file
                             )
    LAUNCHER.make_directory()
    LAUNCHER.make_file(ARGS.script_file)
    LAUNCHER.make_file(ARGS.readme_file)
    LAUNCHER.make_file(ARGS.license_file)
    LAUNCHER.make_file(ARGS.requirements_file)
    LAUNCHER.make_file(ARGS.gitignore_file)
    print("Execution completed.")
