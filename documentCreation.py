

import sys
import subprocess
import re

def libreoffice_exec():
    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    else:
        print(sys.platform)
    return 'libreoffice'

def convert_to(source,timeout=None):
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', source]
 
    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    print(process)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())
    print(filename)
    return filename.group(1)
