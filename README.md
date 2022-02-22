# Password Word Generator (PWG)

PWG is a small function with Command Line (CLI) and Graphical (GUI) interfaces.

Back end and CLI are built with Python and included libraries, while the GUI is built with the included Tkinter.

The program uses a dictionary file to generate easy-to-remember passwords using whole words, a concept described in [XKCD 936](https://xkcd.com/936/).

The dictionary file is sourced from [gwicks.net](http://www.gwicks.net/dictionaries.htm), including various words of various lengths.

---

## Dependencies
- None, all libraries used are included in default Python installation.

---

## Usage

Please note that larger words occur less and less frequently. The dictionary used has words as long as 26 letters, however the generator does not work well with words at either extreme. 

Given inputs are length of password (in characters) and number of whole words desired.

Currently, the generator uses a single word length as often as possible.

Todo: implement varying word lengths

---

![CLI image](/img/img_cli.png)

CLI can be accessed by running `main_cli.py`

---

![GUI image](/img/img_gui.png)

GUI can be accessed by running `main_gui.py`

---