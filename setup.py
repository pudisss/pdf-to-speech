from setuptools import setup, find_packages


with open("README.md", "r") as readme:
    description = readme.read()

setup(
    name="pypdftospeech",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "pypdf==5.3.1",
        "pyttsx3==2.98"
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)