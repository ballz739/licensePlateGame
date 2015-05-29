###
#
# (C) Copyright 2015
#
###

from distutils.core import setup

setup(
    #application name
    name='licensePlateGame',

    #version (Major.Minor.ChangeSet)
    version='0.1.0',

    #application author
    author='Robert Balala',
    author_email='rlbalala@gmail.com',

    #license
    license='MIT',

    #keywords
    keywords='example python development'

    #packages
    packages=find_packages(exclude=['test']),

    data_files=[('statesDat', ['data/licenseplategame.dat']),
                ('statesXml': ['data/licenseplategame.xml'])
    ],

    #include addl files into package
    #include_package_data=True,

    #details
    url='',

    #description
    description='Game to play when you are road tripping across the country'
    #long_description=open('ReadMe.txt').read(),

    #dependent packages (distributions)
    #install_requires=[
    #    'xxxx',
    #]
    )
