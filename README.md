# pyqt

Build GUI application

```bash
pip install pyqt5
```

## Build distribution using pyinstaller

To make a distributable package using `pyinstaller`, you need to build the python verion using below:

```bash
env PYTHON_CONFIGURE_OPTS="--enable-framework" SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk MACOSX_DEPLOYMENT_TARGET=10.14 pyenv install 3.6.8
```

And after that, for some reason the pyinstall command will not be available...To work this around, run

```bash
python -m PyInstaller cli.py

```

and it should work!
