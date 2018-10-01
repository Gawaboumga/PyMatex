import setuptools

setuptools.setup(
    name='pymatex',
    version='0.0.3',
    author='Gawaboumga',
    description='Python parser for latex mathematical expression',
    url='https://github.com/Gawaboumga/PyMatex',
    packages=setuptools.find_packages(),
    install_requires=['antlr4-python3-runtime'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
