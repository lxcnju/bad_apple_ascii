#-*- coding:utf-8 -*-

# asciiÂë±í
def load_ascii(fpath):
    f = open(fpath, 'r', encoding = 'utf-8')
    ascii_list = [asc.strip() for asc in f.read().split() if len(asc.strip()) > 0]
    return ascii_list