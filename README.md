D64niceGUI is an UI for the existing commandline tool D64nice

D64nice is used for beautifying Dirart by replacing Pipe and Line chars with signs, which exists in the lower and upper PETSCII ROM Char of the C64

D64niceGui is an Windows UI für the commandline tool, which makes it easier to fulfill tasks like:

- Batch calls
- Error handling
- Definition of Postfix or Prefix for files
- also it brings some color to your life :-)

The tool itself is a python beginners project, if you find bugs, feel free to correct them :-)

Idea: B4r4cud4 of BLAZON
Help: Logiker of Vintage Computing Carinthia
Code: Freeze of BLAZON

Getting started:

- Download d64nice.exe from https://csdb.dk/release/?id=182677 (or try search on https://csdb.dk)
- Download d64niceGUI.exe
- move both exe files into the same folder
- start d64niceGUI.exe

How it works:
- on the left side you can select a target dir where your source d64 files are situated
- on the right side you can specify the output folder, prefix or postfix for the processed files
  - if you select only one file, you can also change the filename
  - if you select multiple files the source file name is used
- with click on "NICE SELECTED" d64nice is called and the files are processed
  - in the information dialog you see the output of d64nice.exe
- if you uncheck the [ ] overwrite existing d64-files then processing will be skipped, if a file with the same filename is given in the output folder

Hint:
- the last used input folder is saved automatically
- the settings for output can be saved manually by using the save buttons
- on the first start, the current folder is used for input and output
  - if the input folder is also the output folder, after processing the files the file list will be updated and the previous selection is removed
  - if the output folder is not the input folder, the selection will be kept
- settings will be stored in the d64niceGUI.json file

- a logfile is also created where you can get further information. Please provide this file with any bug report!

## Development

```bash
git clone --recursive https://github.com/Freeze-blz/toolbox
cd toolbox
python -m venv ./venv
source venv/bin/activate (Windows: venv/Scripts/activate.ps1)
pip install -r requirements.txt
```

HAVE FUN!


