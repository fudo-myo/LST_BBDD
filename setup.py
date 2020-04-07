from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="lst_bbdd_ucm",
    package_dir={'': 'LST_BBDD_MODEL'},
    packages=find_packages(where='LST_BBDD_MODEL'),
    version="1.0",
    description="Project to manage the LST telescope database",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Francisco Javier Romero Lobato",
    author_email="franrome@ucm.es",
    url="https://github.com/fudo-myo/LST_BBDD",
    license='MIT',
    keywords=["lst telescope"],
    python_requires='>2.7'
)
