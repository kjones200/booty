from setuptools import setup, find_packages
import os

# ---------------------------------
# imports the version from the package
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'readme.rst')) as f:
    README = f.read()
exec(open(os.path.join(here, 'booty/version.py')).read())

# ---------------------------------
# project requirements
requirements = [
    'click >= 6.7',
    'intelhex >= 2.1',
    'pyserial >= 3.3'
]

# ---------------------------------
# project setup
setup(
    name='booty',
    version=__version__,
    description='Bootloader application',
    long_description=README,
    author='Jason R. Jones',
    author_email='slightlynybbled@gmail.com',
    url='https://github.com/slightlynybbled/booty',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={'console_scripts': ['booty = booty.__main__:main']},
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English'
    ],
    keywords='bootloader pic24 dspic'
)
