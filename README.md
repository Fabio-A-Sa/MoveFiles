# Photo Organizer with Python and C++

<br/>
<br/>

<p align="center">
  <img width="460" height="300" src="https://i.pinimg.com/originals/b7/ba/38/b7ba3835f63380fbb822669f8f904f11.jpg">
</p>

<br/>
<br/>

## Prerequisites

You need to install the Python extension and all dependences:

```
Python 3.X <-- Python3
pip install Pillow <-- Installing a Python Imaging Library
pip install pyinstaller <-- For utility task in Windows
```


## Running

To run a script, in Linux or Windows, call the script inside a folder with photos using terminal.

```
git clone https://github.com/Fabio-A-Sa/Photo-Organizer.git <-- To add files in your own local repository
cd .\Photo-Organizer\Scripts\
python3 organizer.py
```


## Motivation for script development

Since I am involved in an activity that implies the manipulation of hundreds of photos and other files, the [Geocaching](https://www.geocaching.com/play/search), I needed to implement a Python script to streamline the photo selection and sharing process. Therefore, uploading to my gallery on the official hobby website, which already has more than 25,000 photos, becomes faster. <br/>
Besides that, the fact that it is responsible for dozens of geocaches spread across Portugal and Spain, which require web pages in HTML, Javascript and CSS, made this project increased to the ``.html`` ``.css`` and ``.js`` extensions in addition to those already implemented ``.jpg`` ``.png`` ``.jpeg``  and  ``.txt`` files.


## Fundamentals

### Metadata and exif

A file (downloading an image from the internet or taking a photo with your phone) always contains important information about its creation - the metadata - which can be accessed through the Python Pillow (PIL) library.

```
from PIL import Image

photo = Image.open("elephant.png")
exif = photo._getexif()

exif = {
          37377: 7.149, 
          36867: '2020:10:18 12:33:53',                 <--- Creation Date
          36868: '2021:02:06 01:05:42',                 <--- Modification Date
          37378: 2.27,                                  <--- Focal Distance
          40961: 1, 
          40962: 3120,                                  <--- Number of pixels (vertical)
          40965: 850, 
          37522: '951268', 
          40963: 4160,                                  <--- Number of pixels (horizontal)
          41495: 2, 
          271: 'HUAWEI',                                <--- Brand of smarthphone that taken a photo
          283: 72.0, 
          34850: 2,
          41987: 0, 
          305: 'ATU-L21 8.0.0.151(C33)', 
          306: '2020:10:18 12:33:53',                   <--- Last Access Date
          41994: 0, 
          272: 'ATU-L21',                               <--- Camera Model
       }
```
To evaluate a photograph it was necessary to use the ```key "36867"``` and to evaluate a download to use the ```key "36868" ```.

### Recursive Search

teste


### Logs

teste

<br/>

## License

This project is licensed under the [MIT License](https://github.com/Fabio-A-Sa/Photo-Organizer/blob/main/Licence).<br/>
<br/>
@ Fábio Araújo de Sá <br/>
2020/2021
