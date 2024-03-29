
from  setuptools import setup,find_packages

with open("readme.txt", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Nikunj-102003362",
    version="0.1.6",
    author="Nikunj Bansal",
    author_email="nikunjbansal0562@gmail.com",
    description="Calculates Topsis Score and Rank them accordingly",
    long_description=long_description,
    keywords=['TOPSIS'],
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
)