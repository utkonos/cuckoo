#!/usr/bin/env python3
# Copyright (C) 2016-2020 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - https://cuckoosandbox.org/.
# See the file 'docs/LICENSE' for copying permission.
"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
import pathlib
import setuptools

setuptools.setup(
    name='Cuckoo',
    version='3.0.0',
    description='Automated Malware Analysis System',
    long_description=pathlib.Path().cwd().joinpath('README.md').open(encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cuckoosandbox/cuckoo',
    author='Stichting Cuckoo Foundation',
    author_email='cuckoo@cuckoofoundation.org',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Security',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Flask',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='cuckoo sandbox automated malware analysis project threat intelligence cert soc',
    packages=['cuckoo'],
    python_requires='>=3.8',
    install_requires=[
        'alembic',
        'androguard',
        'beautifulsoup4',
        'chardet',
        'click',
        'cryptography',
        'django',
        'django_extensions',
        'dpkt',
        'egghatch',
        'elasticsearch',
        'flask',
        'flask-sqlalchemy',
        'httpreplay',
        'ipaddress',
        'gevent',
        'jinja2',
        'jsbeautifier',
        'oletools',
        'peepdf',
        'pefile',
        'pillow',
        'pyelftools',
        'pyguacamole',
        'pymisp',
        'pymongo',
        'python-dateutil',
        'python-magic',
        'requests',
        'roach',
        'scapy',
        'sflock',
        'sqlalchemy',
        'unicorn',
        'wakeonlan',
        'weasyprint',
        'yara-python',
    ],
    extras_require={
        'distributed': [
            'psycopg2',
        ],
        'postgresql': [
            'psycopg2',
        ],
    },
    entry_points={
        'console_scripts': [
            'cuckoo=cuckoo.main:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/cuckoosandbox/cuckoo/issues',
        'Source': 'https://github.com/cuckoosandbox/cuckoo',
    },
)
