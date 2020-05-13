import os
import re
import sys
import datetime

version_re = re.compile("^__version__.*=.*\"(.*)\"$")
AUTHOR  = os.getenv('REALNAME')
YEAR = datetime.datetime.now().year

VERSION = "pylitproject/__version__.py"

def main():
    vstring = "0.0.0"
    if os.path.isfile(VERSION):
        fin = open(VERSION,'r')
        lines = fin.readlines()
        lc = 0
        for l in lines:
            m = version_re.match(l)
            if m:
                vstring = m.group(1)
                break
            lc+=1
        fin.close()
    else:
        lines = []
        lines.append("# Copyright %d %s\n\n" % (YEAR, AUTHOR))
        lines.append("__version__ = %s\n" % vstring)
        lc = 2
        vstring="0.0.0"
    major,minor,build = vstring.split('.')
    try:
        inc_opt = sys.argv[1]
    except:
        inc_opt = "build"
    if inc_opt == "version":
        print("Current version:",vstring)
        return
    if inc_opt == "major": major = str(int(major)+1)
    elif inc_opt == "minor": minor = str(int(minor)+1)
    else: 
        if '-' in build:
            bval, tag = build.split('-')
            bval = int(bval) + 1
            build = str(bval) + '-' + tag
        else:
            bval = int(build)+1
            build = str(bval)
    vstring = major + '.' + minor + "." + build

    fout = open(VERSION,'w')
    lines[lc] = "__version__ = \"%s\"" % vstring
    for l in lines:
        fout.write(l)
    fout.write("\n");
    fout.close()

    # update README
    fin = open("README.rst")
    lines = fin.readlines()
    fin.close()

    fout = open('README.rst','w')
    vline = lines[0]
    parts = vline.split()
    projname = parts[0]
    title = '%s (v%s)' % (projname, vstring)
    tline = '#' * len(title)
    fout.write('%s\n' % title)
    fout.write('%s\n' % tline)
    for l in lines[2:]:
        fout.write(l)
    fout.write("\n");
    fout.close()


main()
