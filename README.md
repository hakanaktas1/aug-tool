

<p align="center">
    <br>
    <img src ="icons\logo.png"/>
    <br>
<p>
 

[![PyPI](https://img.shields.io/badge/aug--tool-v0.0.1-blue)](https://pypi.org/project/aug-tool/)
[![Supported Python Versions](https://img.shields.io/badge/python%20-3-blue)](https://pypi.python.org/pypi/Augmentor)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](LICENSE)

# AUG-TOOL: Image Augmentation Tool for Machine Learning Projects 

Aug Tool is a Python library available on PyPI that simplifies image data augmentation for machine learning tasks, compatible with TensorFlow, PyTorch, and the YOLO library.

## Installation


```python
pip install aug-tool
```

To install "aug-tool", you can use pip, the Python package manager. Open a terminal or command prompt and run the following command:


## Features

* Supports various image  augmentation techniques suitable for real environment conditions, such as adding noise, scaling, shifting, and more.
* Provides convenient integration with popular machine learning libraries such as **TensorFlow**, **Keras**, **PyTorch**, etc.
* Allows augmentation of both images and their annotation files in formats such as XML, or TXT. 
* Customizable augmentation parameters, including rotation angle, scaling factor, flipping direction, and more.

## Output examples

|            | Labeled data | With aug tool |
|------------|----------|----------|
| **Example 1**    | <img src="icons\exampleImg.png" alt="Alt Text" width="300" height="225">   | <img src="icons\example.gif" alt="Alt Text" width="300" height="225">   |
| **Example 2**    | <img src="icons\example4.png" alt="Alt Text" width="300" height="250"> | <img src="icons\example4.gif" alt="Alt Text" width="300" height="250"> |
| **Example 3**    | <img src="icons\example2Img.png" alt="Alt Text" width="300" height="200">    | <img src="icons\example2.gif" alt="Alt Text" width="300" height="200"> |
| **Example 4**    | <img src="icons\example3.png" alt="Alt Text" width="300" height="200">    | <img src="icons\example3.gif" alt="Alt Text" width="300" height="200"> |


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

### Package Structure Diagram:

```python
src/ #root file
└── aug_tool/ #main package
    ├── __init__.py
    ├── dataOpener/ #sub package1
    │   ├── __init__.py
    │   ├── dataOp.py
    │   ├── imgOp.py
    │   ├── annOp.py
    │   ├── xmlOp.py
    │   └── txtOp.py
    ├── dataAugmentor/ #sub package2
    │   ├── __init__.py
    │   ├── dataAug.py
    │   ├── imgAug.py
    │   ├── annAug.py
    │   ├── xmlAug.py
    │   └── txtAug.py
    ├── dataSaver/ #sub package3
    │   ├── __init__.py
    │   ├── dataSav.py
    │   ├── imgSav.py
    │   ├── annSav.pys
    │   ├── xmlSav.py
    │   └── txtSav.py
    └── augmentation.py
```
### Class Diagram:

<p align="center">
    <br>
    <img src ="doc\Aug_class_diagram.drawio.png"/>
    <br>
<p>

### Augmentation Class Initialization:

```python
class Augmentation(object):
    def __init__(self, open_data_path:str, save_file_name:str, number_of_aug:int, x_shift:int, y_shift:int) -> None:
        """
        This is an initialization function that takes in parameters for data augmentation and saves the
        augmented data and annotations to a specified file path.
        
        :param open_data_path: The path to the directory containing the original data to be augmented
        :type open_data_path: str
        :param save_file_name: The name of the folder where the augmented data will be saved
        :type save_file_name: str
        :param number_of_aug: The number of times the image and its corresponding annotation will be
        augmented
        :type number_of_aug: int
        :param x_shift: The amount of horizontal shift to apply during image augmentation
        :type x_shift: int
        :param y_shift: y_shift is a parameter that determines the maximum number of pixels by which an
        image can be shifted vertically during data augmentation
        :type y_shift: int
        """  
```
The `__init__` method of the augmentation class performs the initialization and processing steps. This process can be divided into three parts:


#### Part 1: File and Folder Creation

In the first part, the method creates the necessary file names and initializes the folder structure for storing the augmented images. This ensures a well-organized output for the augmented data.

```python
        # It creates a folder to save inside 
        self.create_dest_folder(self.target_file_name)
        
        # All the data in the file is taken and augmented in a loop
        for data_path in self.create_list_of_data(open_data_path = open_data_path):
            
            # The image and label file with the same name as image is opened once
            image = self.label_factory(data_path[:-4])
            label = self.image_factory(data_path)
            
            # The augmentation process is performed as much as the `number_of_aug` value  from the user
            for num in range(number_of_aug):
                
                # The name of new file that will be augmented is created
                data_name = data_path.split("\\")[-1][:-4] + "_aug" + str(num + 1))

```

Here, The `self.create_dest_folder` method is responsible for creating the output folder if it doesn't already exist. `self.create_list_of_data` stores the path of the files which will be augmented . The loop iterates over the files in the `self.create_list_of_data` list and obtains the paths to the corresponding image and label files. The `self.label_factory` and `self.image_factory` methods are responsible for opening the image and label files, respectively.

#### Part 2: Image Augmentation Processing
The second part of the `__init__` method performs the actual augmentation processing of images. Within a nested loop, the augmentation techniques are applied to the image to generate multiple augmented versions of the data.

```python
                # The augmented image is created acording values that given users
                aug_image = dataAugmentor.ImgAug(image=image,
                                                        x_shift=x_shift,
                                                        y_shift=y_shift).image_aug
                                
                # The augmented image is saved on target file   
                dataSaver.ImgSav(target_file_path = self.target_file_name,
                                    img_aug = aug_image,
                                    data_name=data_name)
```

#### Part 3: Label Augmentation Processing
The third part of the `__init__` method performs the actual augmentation processing of labels. Within a nested loop, the augmentation techniques are applied to the label data to generate multiple augmented versions of the data.

```python             
                # If the extension of the read label file is '.xml', it is processed here
                if self.ann.ext == ".xml":
                    
                    ann_aug = dataAugmentor.XmlAug(name=data_name,
                                                annotate= label.data,
                                                x_shift=x_shift,
                                                y_shift=y_shift)
                    
                    dataSaver.XmlSav(target_file_path = self.target_file_name,
                                                                ann_aug=ann_aug.annotate,
                                                                data_name=data_name)

                # If the extension of the read label file is '.txt', it is processed here    
                elif self.ann.ext == ".txt":
                    
                    ann_aug = dataAugmentor.TxtAug(
                                                annotate= label.data,
                                                x_shift=x_shift,
                                                y_shift=y_shift,
                                                width=aug_image.width,
                                                height=aug_image.height).aug_anotate
                    
                    dataSaver.TxtSav(target_file_path = self.target_file_name,
                                     ann_aug=ann_aug,
                                    data_name=data_name)
```

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this library in accordance with the terms specified in the license.

## Support
If you have any questions, suggestions, or need support, feel free to reach out to hakanaktas4541@gmail.com
