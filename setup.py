import os

from setuptools import setup, find_packages

import lendingblock


def read(name):
    filename = os.path.join(os.path.dirname(__file__), name)
    with open(filename) as fp:
        return fp.read()


meta = dict(
    version=lendingblock.__version__,
    description=lendingblock.__doc__,
    name='lb-py',
    author='Luca Sbardella',
    author_email="luca@lendingblock.com",
    maintainer_email="luca@lendingblock.com",
    url="https://github.com/lendingblock/lb-py",
    license="BSD",
    long_description=read('readme.md'),
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['aiohttp'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
    ]
)


if __name__ == '__main__':
    setup(**meta)
