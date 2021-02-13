# Photo Organizer with Python and C++

<p align="center">
  <img width="460" height="300" src="https://i.pinimg.com/originals/b7/ba/38/b7ba3835f63380fbb822669f8f904f11.jpg">
</p>

### Prerequisites

What things you need to install the software:

```
git clone https://github.com/Fabio-A-Sa/Photo-Organizer.git
```

```
Python 3.X <-- Python3
pip install Pillow <-- Installing a Python Imaging Library
pip install pyinstaller <-- For utility task in Windows
```

## Running the tests

### Linux, Mac OS X, BSD and most OSes except Windows
Turn script executable:

```
chmod +x photo-organizer.py
```

Call script inside a folder with photos:

```
./photo-organizer.py .
```

### Windows

To run a test, call the script inside a folder with photos.

```
python photo-organizer.py .
```

**For Windows in Context Menu:**

1. To generate *photo-organizer.exe* file to run on Windows.

```
pyinstaller -w -F photo-organizer.py
```

2. Add the keys on Registry or run *photo-organizer.reg*.
3. Copy .exe file on *C:\Program Files\Photo Organizer*
4. Add *C:\Program Files\Photo Organizer* in the *Path* on Windows Environment Variable.

## License

This project is licensed under the [MIT License](something.com).<br/>


@ Fábio Araújo de Sá <br/>
2020/2021
