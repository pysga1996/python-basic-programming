import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="basic_io",
    version="0.0.1",
    author="pysga1996",
    author_email="pysga1996@gmail.com",
    description="Python Input/Output and comment demo ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pysga1996/python-basic-programming.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
