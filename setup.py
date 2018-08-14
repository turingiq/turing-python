import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="turing_api",
    version="1.0.0",
    author="Turing Analytics",
    author_email="aditya@turingiq.com",
    description="Turing visual search and visually similar recommendations API library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/turingiq/turing-python",
    packages=setuptools.find_packages(),
    install_requires=['requests==2.*'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
