

<p align="center">
    <br>
    <img src ="icons\logo.png"/>
    <br>
<p>


[![PyPI](https://img.shields.io/badge/aug--tool-v0.0.1-blue)](https://pypi.org/project/aug-tool/)
[![Supported Python Versions](https://img.shields.io/badge/python%20-3-blue)](https://pypi.python.org/pypi/Augmentor)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](LICENSE)

# AUG-TOOL: Image Augmentation Tool for Machine Learning Projects 

Seamlessly integrate powerful language models like ChatGPT into scikit-learn for enhanced text analysis tasks.

## Installation


```python
pip install aug-tool
```

To install "aug-tool", you can use pip, the Python package manager. Open a terminal or command prompt and run the following command:


## Features

* Supports various image  augmentation techniques suitable for real environment conditions, such as adding noise, scaling, shifting, and more.
* Provides convenient integration with popular machine learning libraries such as **TensorFlow**, **Keras**, **PyTorch**, etc.
* Allows augmentation of both images and their annotation files in formats such as XML, or TXT. (json will be added soon)
* Customizable augmentation parameters, including rotation angle, scaling factor, flipping direction, and more.

* Supports augmentation of multiple images and annotation files in batch mode.

## Documentation
### Simple usage:
```python
from aug_tool import Augmentation

# Specify the input parameters
open_file_name = r"C:\Users\user.name\Desktop\datas\orginal" #Path to the data folder

save_file_name = r"C:\Users\user.name\Desktop\datas\augmented"#Path to the data folder

number_of_aug = 2 # Number of augmented data to generate

# Apply data augmentation using aug-tool
Augmentation(open_data_path=open_file_name,
        save_file_name=save_file_name,
        number_of_aug=number_of_aug,
        x_shift=15,
        y_shift=15)

 # Continue with further processing or analysis
```

### Package Structure: