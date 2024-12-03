"""Setup for the Pre-Kirshor"""
from setuptools import setup, find_packages
from Cython.Build import cythonize

with open(
  "README.md",
  "r") as fh:
  long_description = fh.read()

_name = "pre-kirshor"
_version = "0.0.0.0.0.0.0.0.0.0.0.1"
_setup_kwargs={
  'name':
    f"{_name}",
  'version':
    f"{_version}",
  'author':
    "Pellegrino Prevete",
  'author_email':
    "pellegrinoprevete@gmail.com",
  'description':
    "Pre-process text for further compression.",
  'long_description':
    long_description,
  'long_description_content_type':
    "text/markdown",
  'url':
    f"https://github.com/themartiancompany/{_name}",
  'packages':
    find_packages(),
  'entry_points': {
    'console_scripts': [
      'pre-kirshor = pre_kirshor:_main']
  },
  'install_requires': [
    'cython',
  ],
  'classifiers': [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    "Operating System :: Unix",
  ],
  'ext_modules':
    cythonize(
      'pre_kirshor/encode.pyx'),
}

setup(
  **_setup_kwargs)
