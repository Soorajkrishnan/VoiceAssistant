import os
from stt import ear
from tts import mouth


def setf():
    mouth("Choose a folder from below")
    mouth("1.Downloads \t 2.Documents \t 3.Pictures\t 4.Music\t 5.Videos")
    mouth("Default is Home Directory")
    fld=home
    destf=ear()
    print destf
    if "download" in destf:
        fld=fld+'/Downloads'
        return fld
    elif "documents" in destf:
        fld=fld+'/Documents'
        return fld
    elif "pictures" in destf:
        fld=fld+'/Pictures'
        return fld
    elif "music" in destf:
        fld=fld+'/Music'
        return fld
    elif "videos" in destf:
        fld=fld+'/Videos'
        return fld
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
    mouth("From which folder folder")
    locf=ear()
    mouth('Which folder do you want to delete ?')
    delf=ear()
