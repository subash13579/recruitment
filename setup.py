# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in recruitment/__init__.py
from recruitment import __version__ as version

setup(
	name='recruitment',
	version=version,
	description='VHRS Custom for Recruitment',
	author='VHRS',
	author_email='hr@voltechgroup.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.req) for ir in requirements],
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
