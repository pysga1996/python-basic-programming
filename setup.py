import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-basic-programming",
    version="0.0.1",
    author="pysga1996",
    author_email="pysga1996@gmail.com",
    description="Python basic programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pysga1996/python-basic-programming.git",
    packages=['basic_input_and_output'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
