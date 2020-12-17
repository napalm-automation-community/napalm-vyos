"""setup.py file."""

from setuptools import setup, find_packages

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines()
            if (len(r) > 0 and not r.startswith("#"))]

__author__ = 'Piotr Pieprzycki <piotr.pieprzycki@dreamlab.pl>'


setup(
    name="napalm-vyos",
    version="0.2.1",
    packages=find_packages(),
    author="Piotr Pieprzycki",
    author_email="piotr.pieprzycki@dreamlab.pl",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation-community/napalm-vyos",
    include_package_data=True,
    install_requires=reqs,
)
