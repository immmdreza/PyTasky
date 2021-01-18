import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTasky",
    version="1.2.0",
    author="immmdreza",
    author_email="ir310022@gmail.com",
    description="Task System api for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/immmdreza/PyTasky",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
