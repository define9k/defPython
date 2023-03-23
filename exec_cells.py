"""
=======================================
# -*- coding: utf-8 -*-
@Project : defPython
@File : exec_cells.py
@Author : ydf
@Date : 2023/3/20 16:50
=======================================
"""
# import numpy
import re
import codecs
import nbformat
import datetime
from nbconvert.preprocessors import ExecutePreprocessor


def job(file_name):
    output = ""
    print(f"The job of crontabs {file_name} starts!")
    # file_handler = FileDataHandlers(MAIN_DIR)
    if file_name.endswith('py'):
        with codecs.open(file_name, mode="r", encoding='utf-8') as file1:
            code = file1.read()
        try:
            exec(code)
            # print("code::", code)
            output = "执行成功"
        except Exception as e:
            print(f"The executing error of {file_name} is {e}")
            output = str(e)
    elif file_name.endswith('ipynb'):
        with open(file_name, encoding='utf-8-sig') as ff:
            nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3', allow_errors=True)
        nb_out = ep.preprocess(nb_in, {"metadata": {"path": "./"}})
        # print("nb_out::", nb_out)
        out_cell = nb_out[0]
        cells_list = len(out_cell['cells'])
        out_put_list = []
        success_key = 0
        for i in range(cells_list):
            if out_cell['cells'][i]['outputs'] and out_cell['cells'][i]['outputs'][0]['output_type'] == 'error':
                print("out_cell['cells'][i]['outputs']", out_cell['cells'][i]['outputs'])
                error_list = out_cell['cells'][i]['outputs'][0]['traceback']
                for error_str in error_list:
                    old_str1 = re.sub(r'\\n', '', repr(error_str))
                    new_str = re.sub(r'\\x1b\[(\d*\W?)*\d*m', '', old_str1)
                    new_str = re.sub(r'\\\\', r'\\', new_str)
                    # re.sub(r'(x1b.*m)', '', out_cell['cells'][i]['outputs'][0]['traceback'][cell])
                    # new_str = re.sub(r'x1b\[1;31m', '', out_cell['cells'][i]['outputs'][0]['traceback'][error_str])
                    print("+++", new_str)
                    out_put_list.append(new_str)
                success_key = 1
        if success_key == 0:
            output = "执行成功"
        else:
            print(f"The executing of {file_name} generates some problems.")
            output = str(out_put_list)
    return output
    # print("-----exec output is----", file_dict)
