#!/usr/bin/env python

from distutils.core import setup

setup(name='Django WIFIDog',
      version='1.0',
      description='A Django implementation of the WIFI Dog captive portal',
      author='Ryan Bagwell',
      author_email='ryan@ryanbagwell.com',
      url='https://github.com/ryanbagwell/django-wifidog',
      packages=['wifidog'],
      install_requires=[
        'django-tastypie == 0.9.15',
      ]
     )