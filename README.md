
=======
# PdfToSpeech package
My package allows you to read pdf and convert those text into speech.
It's a simple project that I decide to create to practice more in Python plus gain experience by creating real world projects.
I'm just a passionate builder who likes building projects. In the future I planned to update more features and to make it more user-friendly.

# Package used
1. [PyPdf][https://pypi.org/project/pypdf/]
2. [Pyttsx3][https://pypi.org/project/pyttsx3/]


# Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)


## Installation
```bash
pip install pypdftospeech
```


## Usage
```python
from pypdftospeech import PdfToSpeech
pdf = PdfToSpeech(filename="filename.pdf", pageNumber=10, incwd=True)

pdf.pdf_to_speech()
```
Arguments.
1. filename - The name of the pdf file
2. pageNumber - The page number that you want the module to read from
3. incwd - Is the file in your working directory?. 

## Features
1. Read your pdf file and then translate it to a speech, output by your computer speaker

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

![License](https://img.shields.io/badge/license-MIT-blue.svg)

