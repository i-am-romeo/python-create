import os
import string


class Create:

    def __init__(self):

        print('i am here to set up your awesome project,')
        self.author = input("so what's your name ").lower()
        self.name_of_project = input('The name of project? ').lower()
        self.name_of_main_module = input('Let me add the main module for you, what would you name it ').lower()
        self.description = input('how about some description ').lower()

        self.create_set_up()
        self.create_module()
        self.create_test()

    def create_module(self):
        module_path = os.path.join(self.name_of_project, self.name_of_main_module)
        if not os.path.isdir(module_path):
            os.makedirs(module_path)
        init_file = open(os.path.join(module_path, '__init__.py'), 'w')

    def create_test(self):
        test_path = os.path.join(self.name_of_project, 'tests', 'w')
        if not os.path.isdir(test_path):
            os.makedirs(test_path)
        init_file = open(os.path.join(test_path, '__init__.py'), 'w')
        app_tests = open(os.path.join(test_path, 'app_tests.py'),'w')

    def create_set_up(self):
        if not os.path.isdir(self.name_of_project):
            os.makedirs(self.name_of_project)
        file_setup = open(os.path.join(self.name_of_project, 'setup.py'), 'w')
        tmplt_setup = '''try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    setup(name = '$name_of_project',
           description='$description',
           author='$author',
           url='',
           download_url='',
           author_email='',
           version='',
             requires=['nose'],
           packages=['$name_of_main_module'],
           scripts=[]
           )'''

        str_setup = string.Template(tmplt_setup).safe_substitute({
            'name_of_project': self.name_of_project,
            'description': self.description,
            'author': self.author,
            'name_of_main_module': self.name_of_main_module})
        file_setup.write(str_setup)

if __name__ == '__main__':
    Create()






