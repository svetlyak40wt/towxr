from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='ToWXR',
      version=version,
      description="Generate WordPress Extended RSS files from various formats.",
      long_description="""\
Currently supported formats are CSV1.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='wordpress wxr import generate csv',
      author='K Belarbi c( commissioned by Anonymous.ag )',
      author_email='k.belarbi@usthb.coselearn.org',
      url='http://anonymous.ag',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
	'console_scripts':
		['towxr = towxr:main']
	}
      )
