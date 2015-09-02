from setuptools import find_packages, setup

import yolapy


setup(
    name='yolapy',
    version=yolapy.__version__,
    description='Python client for the Yola API',
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
