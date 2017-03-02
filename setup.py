from setuptools import setup

setup(name= "LEDTest",
    version="0.1",
    description="LED Testing for Assignment3 in COMP30670 2017",
    url="",
    author="Shanming Li",
    author_email="shanming.li@ucdconnect.ie",
    license='GPL3',
    packages=['src'],
    entry_points={
        'console_scripts':['LEDTest=src.main:main']
        },
    install_requires=[
        'numpy',
        'argparse',
        ]  
    )