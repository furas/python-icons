#!/usr/bin/env python3

from pathlib import Path
from shutil import copy

data = [
    '',
    'Aqua', 
    'Blue', 
    'Brown', 
    #'Dark', 
    'Grey', 
    'Orange', 
    'Pink', 
    'Purple', 
    'Red', 
    'Sand', 
    'Teal', 
    'Yellow', 
]

src_folder = Path('/usr/share/icons')

for color in data:
    if color:
        src_name = src_folder / ('Mint-X-' + color) / 'places' / '48' / 'folder.svg'
    else:
        src_name = src_folder / 'Mint-X' / 'places' / '48' / 'folder.svg'
    print(src_name)

    #dst_folder = Path(color + '-places-48')
    dst_folder = Path('Mint-X')
    print(dst_folder)
    dst_folder.mkdir(parents=True, exist_ok=True)

    if color:
        dst_name = dst_folder /  (color + '-folder.svg')
    else:
        dst_name = dst_folder /  'folder.svg'
        
    print(dst_name)
    copy(src_name, dst_name)
