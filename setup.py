# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='xpoity',
    version="1.31",
    packages=find_packages(),
    author="xpoit",
    install_requires=["argparse","requests","phonenumbers","pycountry"],
    description="It is a tool written to retrieve private information such as Phone Number, Mail Address, ID on Instagram accounts via API.",
    long_description="It is a tool written to retrieve private information such as Phone Number, Mail Address, ID on Instagram accounts via API.",
    include_package_data=True,
    url='http://github.com/xpoit/xpoity',
    entry_points = {'console_scripts': ['xpoity = xpoity.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
