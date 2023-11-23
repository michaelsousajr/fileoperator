from setuptools import setup, find_packages

setup(
    name="fileops",
    version="0.1.0",
    author="Michael Sousa",
    author_email="ms22dq@fsu.com",
    description="An all-in-one utility package for file operations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/michaelsousajr/fileops",  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        "cryptography",
        "pyperclip",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # Or any other license you choose
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
