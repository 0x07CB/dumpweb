#!/usr/bin/python3
#coding: utf-8
#==================================================
import os, argparse
#==================================================
parser = argparse.ArgumentParser()
parser.add_argument("webpath", help="full web adress and path(exemple: https://www.mywebsite.com/index.html)",
                    type=str)
args = parser.parse_args()
#==================================================
fullwebpath = args.webpath
#==================================================
commande_wget = "wget --recursive --no-clobber --page-requisites --html-extension --convert-links --domains {} --no-parent {}"
domaine = fullwebpath.strip()
try:
    domaine = domaine.split("https://")[1]
except:
    pass
try:
    domaine = domaine.split("/")[0]
except:
    pass
os.system(commande_wget.format(domaine,fullwebpath))
