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
{36864: b'0210', 
 37121: b'\x01\x02\x03\x00', 
 37377: 7.149, 
 36867: '2020:10:18 12:33:53', 
 36868: '2020:10:18 12:33:53', 
 37378: 2.27, 
 37379: 0.0, 
 37380: 0.0, 
 37383: 2, 
 37384: 0, 
 37385: 0, 
 37386: 3.46, 
 40961: 1, 
 40962: 3120, 
 40965: 850, 
 41991: 0, 
 37520: '951268', 
 37521: '951268', 
 37522: '951268', 
 40963: 4160, 
 41996: 0, 
 257: 4160, 
 258: (8, 8, 8), 
 41495: 2, 
 271: 'HUAWEI', 
 41728: b'\x03', 
 33434: 0.007029658, 
 282: 72.0, 
 531: 1, 
 33437: 2.2, 
 41729: b'\x01', 
 283: 72.0, 
 42016: '7e9f6d2e276f26290000000000000000', 
 34850: 2, 
 41985: 1, 
 34855: 100, 
 296: 2, 
 41986: 0, 
 40960: b'0100', 
 256: 3120, 
 41987: 0, 
 305: 'ATU-L21 8.0.0.151(C33)', 
 306: '2020:10:18 12:33:53', 
 41989: 26, 
 41992: 0, 
 41993: 0, 
 41994: 0, 
 272: 'ATU-L21', 
 34665: 250, 
 530: (2, 2)}
}
```


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
