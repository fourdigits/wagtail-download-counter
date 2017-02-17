#!/usr/bin/env python
from setuptools import find_packages, setup

tests_require = [
    'coverage==4.2',
    'factory-boy==2.7.0',
    'flake8==3.0.4',
    'isort==4.2.5',
    'pytest==3.0.2',
    'pytest-django==3.0.0',
    'pytest-warnings==0.1.0',
    'mock==2.0.0'
]


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
        'Development Status :: 1 - Planning',
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
    tests_require=tests_require,
    extras_require={
        'test': tests_require
    },
)
