"""
The core of the Voice Assistant

Finds keywords in the input sentence,
then calls the appropriate functions.
"""
# imports
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
import time
import webbrowser
from tts import mouth
from stt import ear
import logging
# Main
home = os.path.expanduser("~")
string=''
def brain():
    string = ear()
    try:
        word_list = word_tokenize(string)
        if "search" in word_list and "google" not in word_list:
            searchs = string.replace('search', '')
            query = 'https://www.google.co.in/search?safe=active&q=' + searchs
            print string
            mouth('Searching...' + searchs)
            webbrowser.open(query)

        elif "mute" in word_list or "volume" in word_list:
            q = os.popen(
                """amixer sget Master | awk -F"[][]" '/dB/ { print $2 }'""").read()
            current_vol = int(q.replace('%', ''))

            if "increase" in word_list or "up" in word_list:
                if current_vol == 100:
                    mouth("Cannot Increasse further")
                else:
                    mouth("increassing Volume")
                    print (os.popen('amixer set Master '
                                    + str(current_vol + 10) + '%').read())

            elif "decrease" in word_list or "down" in word_list:
                if current_vol == 00:
                    mouth("Cannot Increasse further")
                else:
                    mouth("decreassing Volume")
                    print (os.popen('amixer set Master '
                                    + str(current_vol - 10) + '%').read())
            elif "mute" in word_list:
                print (os.popen('amixer set Master 0%').read())
                mouth("Muted")
        elif "folder" in word_list or "directory" in word_list:
            if "make" in word_list or "create" in word_list:
                fol=setf()
                mouth("What name do you want to give ?")
                makef(fol)
            elif "remove" in word_list or "delete" in word_list:
                remf()
        elif "shutdown" in word_list or "turn off" in word_list:
                mouth("Are you sure to shutdown")
                confirm=ear()
                if confirm=='yes':
                    os.popen('shutdown')
                    mouth("System will shutdown in a minute")
                else:
                    mouth("Thank you for not tuning me off.")
        elif "reboot" in word_list or "restart" in word_list:
                mouth("Are you sure to shutdown")
                confirm=ear()
                if confirm=='yes':
                    os.popen('systemctl reboot -i')
                    mouth("Rebooting")
                else:
                    mouth("Thank you for not tuning me off.")
        elif "file" in word_list:
            pass
    except Exception as e:
        logging.error(e.message)



#functions
def setf():
    mouth("Choose a folder where do you want to do folder opearations")
    mouth("Download \t Document \t Picture\t Music\t Video \t Desktop")
    mouth("Default is Home Directory")
    fld=home
    destf=ear()
    print destf
    if "download" in destf:
        fld+='/Downloads'
        return fld
    elif "document" in destf:
        fld+='/Documents'
        return fld
    elif "pictures" in destf:
        fld+='/Pictures'
        return fld
    elif "music" in destf:
        fld+='/Music'
        return fld
    elif "videos" in destf:
        fld+='/Videos'
        return fld
    elif "desktop" in destf:
        fld+='/Desktop'
    else:
        return fld


def makef(name):
    fol=name
    os.chdir(fol)
    fname = ear()
    fname = fname.replace(" ", "_")
    print fname

    if os.path.isdir(fol + '/' + fname) == True:
        mouth("oops Folder already exist")
        mouth("Choose another Name")
        makef()
    else:
        out = os.popen('mkdir ' + fname)
        mouth("%s has been created in %s Directory" % fname %fol)

def remf():
    setd=setf()
    os.chdir(setd)
    dir=os.listdir(os.path.isdir(setd))
    print dir
    mouth('Which folder do you want to delete ?')
    delf=ear()


brain()
