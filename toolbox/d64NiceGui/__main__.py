#                            D64niceGui.py
#                          brought to you by
#
# *********************************************************************
# *                                                                   *
# *  ########   ###         #####    #########    #####    ###   ###  *
# *  ###   ###  ###       ###   ###       ###   ###   ###  ####  ###  *
# *  ###   ###  ###       ###   ###      ###    ###   ###  ##### ###  *
# *  ######     ###       #########     ###     ###   ###  ### #####  *
# *  ###   ###  ###       ###   ###    ###      ###   ###  ###  ####  *
# *  ###   ###  ###       ###   ###   ###       ###   ###  ###   ###  *
# *  ########   ######### ###   ###  #########    #####    ###   ###  *
# *                                                                   *
# *     (c) 2022 by FREEZE of BLAZON; Idea: B4r4cud4 of BLAZON        *
# *   Thanks for helping hand and the main tool to Logiker / VCC      *
# *********************************************************************
#
# This tool is open source, feel free to expand the functionality or
# fix bugs you may find :-)
#
# Now let's start the action...


# Import needed modules - if not installed you have to pip PySimpleGui and EasyProcess

import logging
import PySimpleGUI as Sg
import os.path
import time

from easyprocess import EasyProcess
from pathlib import Path
from os.path import exists
import win32api

logging.basicConfig(
    format="%(asctime)s %(message)s",
    filename="d64NiceGui.log",
    encoding="utf-8",
    level=logging.INFO,
)
version = "V 1.1.5"
release = "Released at VCC $1C 19/11/22"

# Console output...
os.system("cls")
print("D64nicerGUI brought to you by BLAZON!")

# reading configuration
configfile = os.getcwd() + "d64nicerGUI.json"

Sg.user_settings_filename("D64nicerGUI.json", os.getcwd())

path = Sg.user_settings_get_entry("lastpath", os.getcwd())
path = path.replace("/", "\\")
lastfolder = path

folder = Sg.user_settings_get_entry("outfolder", os.getcwd())
folder = folder.replace("/", "\\")

nicedprefix = Sg.user_settings_get_entry("nicedprefix", "D64niced_")
nicedpostfix = Sg.user_settings_get_entry("nicedpostfix", "")

# base definition of window layout
Sg.theme("DarkBlue4")
logo = b"iVBORw0KGgoAAAANSUhEUgAAAUEAAABOCAYAAAC+L6RQAAAEAElEQVR4nO3d0ZKbMBBEUZza//9l8mATEy/YgKWZ1vQ9T6nKbiwkTSMQONMEAAAAAAAAAAAAAAAAAAAAAAXdshtQzTzP8/Ln2+1G/wLifnr9w+swmKaagfAaeK/HDEBfkxB0KH6HYwQcnQ5BhzBwOEYAd29D0CEMHI4RwL5/IUgYAHD0J7sBAJCJEARgjRAEYI0QBGCt28PSZ83zPB954LjiQ9cA8qSF4NXd6OX3ljD8Zlc7IlCVdt3PvNWy1TdKx6Lm6lza6tMrbx+1mstRY9zjDaurfRAegq0OvGUY4re94nz39/isV785vKb6ydU+CA3BHhOAMIyz9eUQ9PexYovup9e6cHT0y0xk7gl+az3oFGZ/nHyOye4XwvDuXT+U2x1eNliy2+Fifrg9ZLcn2rtjzg7ANaW2ZNrqh3IhOE0EYYZ1GGa3RYFi6Ci2KcNrP5QMwWkiCLM49fvecSqHjXLbIq37If2eYM+CUSjI7M/PoNDvLVwJjCu/E91XKuOjcishLQSjBkFlwN1E35BvWTRXH9o/04bsOUldPPsg5XI448wX+XmIpTC+Zx5CVwkfhX5TEB6CKhMA2NLz1U3FuU8QFt4YecVg16QwrkfaoBiAuAsNweyJoFAw0OX6BR7udWGzEkQ9oxRvxeCsxC4ERykcxIrYEYam9OcEcc43RVdpRUL4oBXLEBzpGSmKvT+3HeEtI9VEa5YhOALCbx99g5YIQTEUeKxvVoGMVQ2EoAgK6hj6Ca3Z7Q4Di97PBbreYxsNIYhhsApED1wOJ6Owc7i+HYLfWAliCGonC7X24DpWgkkiioiVzLaIVSB9Pw5WgpDHqgs9EYKwEnUvkOAeByEIaaphwuVuHYQgbLAjjC2EIGSprgKPGr39LghBWGAViD2WIchk1zfCKop5VINlCMJL5ipwhDB3RwhCDsGBSHYhyCWMF4Vvihkh1J3rwi4EoW2EwEAthCDKiroXWGU16MoqBJ2X/COoHhTVj29UfItMR3uTnjDuL3pH+MjnTZP3/+qmymYlyMTT5rRKUjtW99oIXQmqDT5qynou8OhqcJqetZAdQNmfr8DiclhtoJdLIk4Kdy37YRnrrDE/O66ZYahWF2uRbSsfgsoDjfYUTixXTnDrn4+Ys1ttjK4VlbEqfU9QOQC5QX6nUAitqY8tVyH/KxuCypNwoV4suE51bAnA30qGoOLk26NaLBGqF+Mytgrju7Sjep9fUS4EFSbcWc5BWN38kDm+S/gRgNvKhKDKGfcbo7f/DLeCzApCVn+fDb87XCU4Xh+VYOLWsw7C3uPLPDpuqBCsEnjv7D03dnYy7/WVwsog+/Mz9T7ZEX4AAAAAAAAAAAAAAAAAAABPfwH9v9xy0Ce9kgAAAABJRU5ErkJggg=="
font = ("Verdana", 8)
buttonicon = ("Courier,14,")

# file list definition
file_list_column = [
    [
        Sg.Text("D64 Folder"),
        Sg.Input(
            path,
            size=(40, 1),
            enable_events=True,
            key="-FOLDER-",
        ),
        Sg.FolderBrowse(
            "📂",
            tooltip="Select source folder for reading D64 files...",
            font=buttonicon,
        ),
        Sg.Button(
            "⟳",
            enable_events=True,
            tooltip="Reload source folder",
            font=buttonicon,
            key="-RELOAD-",
        ),
    ],
    [
        Sg.Listbox(
            values=[],
            enable_events=True,
            select_mode="extended",
            size=(63, 28),
            key="-FILE LIST-",
            highlight_background_color="green"
        )
    ],
    [Sg.Text("🛈 You can select multiple files using CTRL or SHIFT ;-)", font=font)],
]

# Action area
action_column = [
    [
        Sg.Text("D64 Output Folder"),
        Sg.In(folder, size=(39, 1), key="-OUTFOLD-"),
        Sg.FolderBrowse(
            "📂",
            tooltip="Select target folder for created D64 files...",
            font=buttonicon,
        ),
    ],
    [Sg.Text("D64 Output Filename (Prefix | Filename | Postfix)")],
    [
        Sg.In(nicedprefix, size=(10, 1), key="-PREFIX-", enable_events=True),
        Sg.In(size=(32, 1), key="-RESULT-", enable_events=True),
        Sg.In(nicedpostfix, size=(10, 1), key="-POSTFIX-", enable_events=True),
        Sg.Text(".d64"),
    ],
    [Sg.Checkbox("Overwrite existing D64-files", default=True, key="-OVERWRITE-",)],
    [
        Sg.Button(
            "✔ NICE SELECTED!",
            key="-NICE-",
            size=(44, 2),
            button_color=(Sg.theme_background_color()),
            font=("Verdana", 12),
            disabled=True,
        ),
    ],
    [Sg.Text("")],
    [
        Sg.Button(
            "🛈",
            size=(1, 1),
            key="-INFO-",
            font=("Arial", 18),
            border_width=0,
            tooltip="get D64nice.exe information...",
            button_color=("white", Sg.theme_background_color()),
        ),
        Sg.Multiline(
            size=(50, 6),
            key="-TOUT-",
            reroute_stdout=True,
            border_width=0,
            autoscroll=True,
            font="Verdana, 11"
        ),
    ],
    [Sg.Text("")],
    [
        Sg.Text("Save output settings:"),
        Sg.Button("Save Output-File Post/Prefix", key="-PREFSAFE-"),
        Sg.Button("Save Output-Folder", key="-OUTSAFE-"),
    ],
    [Sg.Text("")],
    [
        Sg.Text(
            "D64niceGUI " + version + " - brought to you by",
            justification="center",
            size=(52, 1),
        )
    ],
    [Sg.Image(data=logo, size=(430, 80))],
    [
        Sg.Text(
            "© 2022 by Freeze of BLAZON - Idea: B4r4cud4 of BLAZON",
            justification="center",
            font=font,
            size=(61, 1),
        )
    ],
    [
        Sg.Text(
            release,
            justification="center",
            font=font,
            size=(61, 1),
        )
    ],
]

# Layout definition - 2 colums, left the file list, right the action block

layout = [
    [
        Sg.Column(file_list_column),
        Sg.VSeperator(),
        Sg.Column(action_column),
    ]
]


# check routine of d64nice exists with error output
def niceexist():
    nicefiletocheck = os.path.join(os.getcwd(), "d64nice.exe")

    message = (
        "🤔 Sorry, but it seems, that the D64nice.exe is missing...\n"
        "Please copy the d64nice.exe to the following folder:\n\n"
        f"{nicefiletocheck}\n\n"
        "You can download d64nice at https://csdb.dk/release/?id=182677\n"
        "(for newer releases please use the search for 'd64nice' on csdb)"
    )

    exist = exists(nicefiletocheck)
    if not exist:
        window["-TOUT-"].update(message)

    return exist


# call routine for d64nice.exe with extended error handling
def callnice(filepath, result):
    if niceexist():

        if exists(result) == True:
            if values["-OVERWRITE-"] == False:
                nicer = (
                    "⚠ ERROR: target file "
                    f"{result} "
                    "exists, overwrite not allowed - skipping file"
                )

                window["-TOUT-"].print(nicer)

                logging.info(nicer)

                window.refresh()
                return
            else:
                try:
                    attr = win32api.GetFileAttributes(result)
                    if attr == 33:
                        nicer = (
                            "⚠ ERROR: target file "
                            f"{result} "
                            "is read only - overwrite not possible - skipping file"
                        )
                        window["-TOUT-"].print(nicer)

                        logging.info(nicer)

                        window.refresh()
                        return
                except:
                    logging.exception("message")
                    pass

        try:
            print ("😎 start NICING "+ filepath +"\r")
            p = EasyProcess('d64nice.exe "' + filepath + '" "' + result + '"').call(
                timeout=2
            )
            logging.debug(p)

            file_exists = exists(result)

            nicer = ""

            if not file_exists:
                nicer = (
                    "[ERROR ⚠] D64nice was not able to create the target file"
                    "- please try again or contact freeze_blz@gmx.at"
                )

            nicer = nicer + p.stdout
            nicer = nicer + " " + result + " " + p.stderr

            window["-TOUT-"].print(nicer)

            logging.info(nicer)

            window.refresh()
        except:
            logging.exception("message")
            pass

    # call routine for help / information output


def callhelp():
    if niceexist():
        try:
            p = EasyProcess("d64nice.exe /?").call(timeout=15)
            logging.debug(p)

            nicer = "D64nice by Logiker of VCC \n \n"

            nicer = nicer + p.stdout

            nicer = nicer.replace("''", "'−'")
            nicer = nicer.replace("long minus", "line")
            nicer = nicer.replace("when \\n", "when")
            nicer = nicer.replace("will \\n", "will")
            nicer = nicer.replace("((", "(")

            nicer = (
                    nicer
                    + (
                        "\n \nNotice: An existing Windows write protection of an existing target file "
                        "stop d64nice from processing and you will get an error output. "
                        "A floppy disk protection in the D64 file will be ignored."
                    )
            )
            nicer = (
                    nicer
                    + "\n \nD64niceGUI "
                    + version
                    + "\n\nCredits:\nCode and logo by Freeze of BLAZON\nIdea: B4r4cud4 of BLAZON\nHelp: B4r4cud4 of BLAZON and Logiker of VCC"
            )
            nicer = (
                    nicer
                    + (
                        "\n \nif you run into an error you cannot solve by yourself, "
                        "feel free to contact me (via email "
                    )
            )
            nicer = nicer + "at freeze_blz@gmx.at.)\n \n"

            print(nicer)
            window["-TOUT-"].update("")
            window["-TOUT-"].update(autoscroll=False)
            window["-TOUT-"].update(nicer, append=True)
            logging.info(nicer)

            window.refresh()
        except:
            logging.exception("message")
            pass


# refresh routine for action block if list selection is more than one file
def listupdate():
    if len(values["-FILE LIST-"]) == 0:
        window["-NICE-"].update(disabled=True)
        window["-NICE-"].update(button_color=Sg.theme_background_color())
    else:
        window["-NICE-"].update(disabled=False)
        window["-NICE-"].update(button_color="green")

    if len(values["-FILE LIST-"]) == 1:
        window["-RESULT-"].update(file)
        window["-RESULT-"].Update(disabled=False)
        window["-RESULT-"].update(text_color="black")
    else:
        window["-RESULT-"].update("⚠ filenames from selection list ⚠")
        window["-RESULT-"].update(disabled=True)
        window["-RESULT-"].update(text_color="gray")

    window.refresh()


# caller method for processing the selected files in the file list
def nicefile(items):
    window["-TOUT-"].update("")

    if len(items) == 1:

        filepath = os.path.join(values["-FOLDER-"], items[0])

        result = (
                values["-OUTFOLD-"]
                + "/"
                + values["-PREFIX-"]
                + values["-RESULT-"]
                + values["-POSTFIX-"]
                + ".d64"
        )

        callnice(filepath, result)

    else:
        for x in range(len(items)):
            item = items[x]

            filepath = os.path.join(values["-FOLDER-"], item)
            item = Path(filepath).stem

            window["-RESULT-"].update(item)
            window.refresh()
            time.sleep(0.2)

            result = (
                    values["-OUTFOLD-"]
                    + "/"
                    + values["-PREFIX-"]
                    + item
                    + values["-POSTFIX-"]
                    + ".d64"
            )

            callnice(filepath, result)

    if values["-FOLDER-"] == values["-OUTFOLD-"]:
        readfiles(values["-FOLDER-"], False)

    listupdate()


# Get list of files in folder, if refresh is set, then the log-info on the window is cleared
def readfiles(folder2read, refresh):
    logging.debug("readfiles")
    logging.debug(folder2read)
    logging.debug(refresh)

    try:
        file_list = os.listdir(folder2read)

    except:
        logging.exception("message")

        file_list = []

    fnames = [
        f
        for f in file_list
        if exists(os.path.join(folder2read, f)) and f.lower().endswith(".d64")
    ]

    window["-FILE LIST-"].update(fnames)
    # window["-FILE LIST-"].update(set_to_index=items)
    Sg.user_settings_set_entry("lastpath", folder2read)

    if refresh:
        window["-TOUT-"].update("")


# limit input size of given UI Element
def inputsize(element, size):
    if len(values[element]) > size:
        window.Element(element).Update(values[element][:-1])


def inputspecialchars(inputString):
    cleanedString = inputString
    cleanedString = cleanedString.replace("/", "")
    cleanedString = cleanedString.replace("*", "")
    cleanedString = cleanedString.replace("?", "")
    cleanedString = cleanedString.replace("\\", "")
    return cleanedString


a = 0

# SHOW THE WINDOW TO THE WORLD....
window = Sg.Window(
    "D64niceGUI - extending D64nice commandline tool from Logiker / VCC",
    layout,
    finalize=True,
)

# read the defined folder once automatically into the file list
if a == 0:
    a = 1
    path = Sg.user_settings_get_entry("lastpath", os.getcwd())
    logging.debug(path)

    if path == "":
        logging.error("No SourcePath")
    else:
        logging.debug(readfiles)
        readfiles(path, True)
        niceexist()
        window.refresh()

# Run the Event Loop

while True:
    event, values = window.read()

    logging.debug(event)
    # Window is closed
    if event == "Exit" or event == Sg.WIN_CLOSED:
        break

    # Info button is clocked
    if event == "-INFO-":
        callhelp()

    # Save the selected output folder
    if event == "-OUTSAFE-":
        try:
            folder = str(values["-OUTFOLD-"] or "")
            folder = folder.replace("/", "\\")

            # if outfolder is not set, use In-Folder
            if folder == "":
                folder = values["-FOLDER-"]

            window["-OUTFOLD-"].update(folder)
            window.refresh()

            Sg.user_settings_set_entry("outfolder", folder)
        except:
            logging.exception("message")
            pass

    # Safe postfix and Prefix Values
    if event == "-PREFSAFE-":
        try:
            Sg.user_settings_set_entry("nicedprefix", values["-PREFIX-"])
            Sg.user_settings_set_entry("nicedpostfix", values["-POSTFIX-"])

        except:
            logging.exception("message")
            pass

    # Call NICE EXE helper routine with selected values from file List
    if event == "-NICE-":
        nicefile(values["-FILE LIST-"])

    # update output path to windows style
    if event == "-OUTFOLD-":
        outfolder = values["-OUTFOLD-"]
        outfolder = outfolder.replace("/", "\\")
        window["-OUTFOLD-"].update(outfolder)

    # Event raised on selection of a new source folder
    if event == "-FOLDER-" or event == "-RELOAD-":

        infolder = values["-FOLDER-"]
        infolder = infolder.replace("/", "\\")

        if event == "-FOLDER-" and lastfolder == infolder:
            lastfolder = infolder
        else:
            window["-FOLDER-"].update(infolder)
            window["-NICE-"].update(disabled=True)
            window["-NICE-"].update(button_color=Sg.theme_background_color())
            readfiles(infolder, True)
            lastfolder = infolder

    if event == "-PREFIX-" or event == "-POSTFIX-":
        window.Element(event).update(inputspecialchars(values[event]))
        inputsize(event, 10)

    if event == "-RESULT-":
        window.Element(event).update(inputspecialchars(values[event]))
        inputsize(event, 50)

    # A file was chosen from the listbox
    elif event == "-FILE LIST-":

        try:
            file = values["-FILE LIST-"][0]
            file = Path(file).stem

            window["-TOUT-"].update("Selected: " + str(len(values["-FILE LIST-"])))

            listupdate()

        except:
            logging.exception("message")
            pass

window.close()
