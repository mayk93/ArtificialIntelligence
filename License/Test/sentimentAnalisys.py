#Refactor: Rewrite with MongoDB

#Libraries
import urllib
from urllib.request import urlopen

import http.cookiejar
from http.cookiejar import CookieJar

import time
import datetime
import re
import sqlite3

"""
Data Base Initialization
"""
'''
#Variables
connection = sqlite3.connect("knowledgeBase.db")
cursor = connection.cursor()
#Functions
def createDB():
    cursor.execute()
'''

'''
Explanations:
links = re.findall(r'<link.*href=\"(.*?)\"',sourceCode)
Here, I say find all strings that match this pattern:
They start with "link."
After any number of characters, they get to ' href=" ': ""*href=\"".
Note: We cannot simply say ' " ', we have to skip it, so we say ' \" '.
After any number of characters, they get to ' ?" '
'''

"""
RSS feed connection
"""
cookieJar = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJar))
opener.addheaders = [('User-agent','Mozilla/5.0')]
connection = sqlite3.connect('knowledgeBase.db')
cursor = connection.cursor()

def checkLine(line):
    test = True
    tags = [ '<img width' , '<a href=' ]
    for tag in tags:
        if tag in line:
            test =  False
            break
    return test

def huffingtonRSSvisit():
    try:
        page = "http://www.huffingtonpost.com/feeds/index.xml"
        sourceCode = opener.open(page).read()
        try:
            links = re.findall(r'<link.*href=\"(.*?)\"',str(sourceCode))
            for link in links:
                if ".rdf" in link:
                    pass
                else:
                    print("Content:")
                    print("###############")

                    linkSource = opener.open(link).read()
                    linesOfInterest = re.findall(r'<p>(.*?)</p>',str(linkSource)) #Note: The preprocessing is very weak

                    for line in linesOfInterest:

                        if( checkLine(line) ):
                            print(line)
                            
        except Exception as e:
            print("Exception in RSS conection - In")
            print(str(e))
    except Exception as e:
        print("Exception in RSS conection - Out")
        print(str(e))

'''
Main
'''
def main():
    huffingtonRSSvisit()

if __name__ == "__main__":
    main()
