import sys
import os

ispy3 = sys.version_info[0] == 3
iswin = os.name == 'nt' 

kwargs = {}
scripts = ["flake8/flake8"]
if ispy3:
    from distutils.core import setup    # NOQA
    if iswin:
        scripts.append("scripts/flake8.cmd")
else:
    try:
        from setuptools import setup    # NOQA
        kwargs = {
            'entry_points':
                {'distutils.commands': ['flake8 = flake8.run:Flake8Command'],
                 'console_scripts': ['flake8 = flake8.run:main']},
            'tests_require': ['nose'],
            'test_suite': 'nose.collector',
        }
    except ImportError:
        from distutils.core import setup   # NOQA
        if iswin:
            scripts.append("scripts/flake8.cmd")

from flake8 import __version__

README = open('README').read()

setup(
    name="flake8 w/doctests",
    license="MIT",
    version=__version__,
    description="Fork of flake8 that adds running of doctest",
    author="Doug Turnbull",
    author_email="softwaredoug@gmail.com",
    url="http://github.com/softwaredoug/flake8_doctests",
    packages=["flake8", "flake8.tests"],
    scripts=scripts,
    long_description=README,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Utilities",
        ],
    **kwargs)
