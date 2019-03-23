import setuptools

with open("README.md", r) as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyReads",
    version="0.0.1",
    author="htwight",
    author_email="",
    description="GoodReads API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/htwight/PyReads",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)