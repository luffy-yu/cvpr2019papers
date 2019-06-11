# !/usr/bin/env python
# @Time    : 2019/6/11 13:56
# @Author  : zej-luffy
# @File    : cvpr2019.py
# @Software: PyCharm

"""
Download CVPR 2019 papers

Using requests_html to parse html
and using wget to download file.
"""

import os

try:
    from requests_html import HTMLSession
except ImportError:
    HTMLSession = None

try:
    import wget
except ImportError:
    wget = None

if not HTMLSession:
    print('Please run "pip install requests_html" first')
    exit(1)

if not wget:
    print('Please run "pip install wget" first')
    exit(1)

__author__ = 'zej-luffy'
__status__ = "dev"
__version__ = "0.1"
__date__ = "2019/6/11"


def main(url, folder):
    # check dir
    if not os.path.exists(folder):
        os.mkdir(folder)

    sess = HTMLSession()
    r = sess.get(url)
    # get all absolute links
    all_absolute_links = r.html.absolute_links
    # filter .pdf links
    pdf_links = list(filter(lambda x: x.endswith('.pdf'), all_absolute_links))
    total = len(pdf_links)
    print('Total : {}'.format(total))
    for idx, link in enumerate(pdf_links, start=1):
        name = link[link.rindex('/') + 1:]
        filename = os.path.join(folder, name)
        # save file
        print('Downloading {} / {} : {}'.format(idx, total, name))
        wget.download(link, filename)
        print('\n')
    print('Finish')
    sess.close()


if __name__ == '__main__':
    url = r'http://openaccess.thecvf.com/CVPR2019.py'
    main(url, './CVPR2019')
