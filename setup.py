
import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except:
    README = ''
    CHANGES = ''

requires = []

setup(
    name='vaud',
    version='0.1',
    description='Simple vk.com audio address decoder',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "License :: OSI Approved :: MIT License",
        ],
    keywords='vk.com audio address decoder',
    author="Zharkov Sergey",
    author_email="sttvpc@gmail.com",
    url="https://github.com/yuru-yuri/vk-audio-url-decoder/",
    license="MIT License (https://opensource.org/licenses/MIT)",
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    tests_require=requires,
    install_requires=requires,
    test_suite="vaud",
)
