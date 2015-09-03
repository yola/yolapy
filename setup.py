from setuptools import find_packages, setup

import yolapy


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

setup(
    name='yolapy',
    version=yolapy.__version__,
    description='Python client for the Yola API',
    long_description='%s\n\n%s' % (readme, changelog),
    author='Yola',
    author_email='engineers@yola.com',
    license='MIT (Expat)',
    url='https://github.com/yola/yolapy',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
