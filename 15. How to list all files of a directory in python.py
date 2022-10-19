from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('/Users/ANIMESH BISWAS') if isfile(join('/Users/ANIMESH BISWAS', f))]
