from setuptools import setup, find_packages
#~ import os, sys, glob, fnmatch

setup(name="OpenOPC",
  version='1.3.1',
  download_url='https://github.com/ingenuitas/OpenOPC/zipball/master',
  description="This is a clone of http://openopc.sourceforge.net modified to be used with distutils",
  keywords='python, opc, openopc',
  url='http://openopc.sourceforge.net',
  license='GPLv2',
  packages = find_packages(exclude=['ez_setup']),
  install_requires=['Pyro','Pyro4'],
  zip_safe = False,
  )
