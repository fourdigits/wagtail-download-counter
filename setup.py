#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='wagtail-download-counter',
    version='0.0.1',
    description='A Wagtail add-on to to keep track of the number of downloads per file',
    author='Four Digits BV',
    author_email='info@fourdigits.nl',
    url='https://github.com/fourdigits/wagtail-download-counter',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    license='BSD',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    install_requires=[
        'wagtail',
    ],
)
