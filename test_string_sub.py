"""
=======================================
# -*- coding: utf-8 -*-
@Project : defPython
@File : test_string_sub.py
@Author : ydf
@Date : 2023/3/22 9:42
=======================================
"""
import re
str_sub = ['\x1b[1;31m---------------------------------------------------------------------------\x1b[0m',
           '\x1b[1;31mNameError\x1b[0m                                 Traceback (most recent call last)',
           'Cell \x1b[1;32mIn [3], line 1\x1b[0m\n\x1b[1;32m----> 1\x1b[0m \x1b[38;5;28mprint\x1b[39m(\x1b[43msafafa\x1b[49m)\n',
           "\x1b[1;31mNameError\x1b[0m: name 'safafa' is not defined",
           '\x1b[1;31m---------------------------------------------------------------------------\x1b[0m',
           '\x1b[1;31mImportError\x1b[0m                               Traceback (most recent call last)',
           'Cell \x1b[1;32mIn [5], line 1\x1b[0m\n\x1b[1;32m----> 1\x1b[0m \x1b[38;5;28;01mimport\x1b[39;00m \x1b[38;5;21;01mpandas\x1b[39;00m \x1b[38;5;28;01mas\x1b[39;00m \x1b[38;5;21;01mpd\x1b[39;00m\n\x1b[0;32m      2\x1b[0m pd\x1b[38;5;241m.\x1b[39mcsv\n',
           'File \x1b[1;32mF:\\Anaconda\\envs\\jl_hope_03\\Lib\\site-packages\\pandas\\__init__.py:16\x1b[0m\n\x1b[0;32m     13\x1b[0m         _missing_dependencies\x1b[38;5;241m.\x1b[39mappend(\x1b[38;5;124mf\x1b[39m\x1b[38;5;124m"\x1b[39m\x1b[38;5;132;01m{\x1b[39;00m_dependency\x1b[38;5;132;01m}\x1b[39;00m\x1b[38;5;124m: \x1b[39m\x1b[38;5;132;01m{\x1b[39;00m_e\x1b[38;5;132;01m}\x1b[39;00m\x1b[38;5;124m"\x1b[39m)\n\x1b[0;32m     15\x1b[0m \x1b[38;5;28;01mif\x1b[39;00m _missing_dependencies:\n\x1b[1;32m---> 16\x1b[0m     \x1b[38;5;28;01mraise\x1b[39;00m \x1b[38;5;167;01mImportError\x1b[39;00m(\n\x1b[0;32m     17\x1b[0m         \x1b[38;5;124m"\x1b[39m\x1b[38;5;124mUnable to import required dependencies:\x1b[39m\x1b[38;5;130;01m\\n\x1b[39;00m\x1b[38;5;124m"\x1b[39m \x1b[38;5;241m+\x1b[39m \x1b[38;5;124m"\x1b[39m\x1b[38;5;130;01m\\n\x1b[39;00m\x1b[38;5;124m"\x1b[39m\x1b[38;5;241m.\x1b[39mjoin(_missing_dependencies)\n\x1b[0;32m     18\x1b[0m     )\n\x1b[0;32m     19\x1b[0m \x1b[38;5;28;01mdel\x1b[39;00m _hard_dependencies, _dependency, _missing_dependencies\n\x1b[0;32m     21\x1b[0m \x1b[38;5;66;03m# numpy compat\x1b[39;00m\n',
           "\x1b[1;31mImportError\x1b[0m: Unable to import required dependencies:\nnumpy: No module named 'numpy'",
           '\x1b[1;36m  Cell \x1b[1;32mIn [7], line 1\x1b[1;36m\x1b[0m\n\x1b[1;33m    e = d + 5x\x1b[0m\n\x1b[1;37m            ^\x1b[0m\n\x1b[1;31mSyntaxError\x1b[0m\x1b[1;31m:\x1b[0m invalid decimal literal\n']
print(type(str_sub[1]))


def filter_str(str_list):
    new_list = []
    for old_str in str_list:
        # old_str1 = re.sub('\\\\n', '', old_str)
        # new_str = re.sub('\\\\x1b\[(\d*\W?)*\d*m', '', old_str1)
        old_str = re.sub(r'(\\x1b\[(\d*\W?)*\d*m)|(\\n)', '', repr(old_str))
        # new_str = re.sub(r'', '', old_str1)
        new_str = re.sub(r'\\\\', r'\\', old_str)
        new_list.append(new_str)
    return new_list
# abc = re.sub('x1b\[1\W31m', '', str_sub[1])


new = filter_str(str_sub)
print("before")
print(str_sub[1])
print("after")
print(new)
