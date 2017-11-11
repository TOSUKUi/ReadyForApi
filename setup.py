from setuptools import setup

def local_requirements():
    req_list = []
    with open('requirements.txt') as requirements_file:
        req_list = [line.strip() for line in requirements_file.readlines()]
    install_reqs = list(filter(None, req_list))
    return install_reqs

setup(name='readyforapi',
      version='1.1.7.3',
      description='An object oriented Python 3.5+ library to get information from readyfor',
      url='https://github.com/TOSUKUi/readyfor-api',
      author='TOSUKUi',
      author_email='',
      license='MIT',
      packages=['readyforapi'],
      install_requires=local_requirements(),
      zip_safe=False)