import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pymatex',
    version='0.0.12',
    author='Gawaboumga',
    description='Parser which allows to parse mathematical expressions written in LaTeX',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Gawaboumga/PyMatex',
    packages=setuptools.find_packages(),
    install_requires=['antlr4-python3-runtime'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
