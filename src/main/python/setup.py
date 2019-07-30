import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nanopar-phelps-sg",
    version="0.0.1",
    author="Steve Phelps",
    author_email="phelps.sg@gmail.com",
    description="A miniminalist parallel map without pickling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phelps-sg/nanopar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
