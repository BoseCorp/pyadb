import os
from distutils.core import setup

setup(
    name = "pyadb",
    version = "0.1.6",
    author = "Chema Garcia",
    author_email = "chema@safetybits.net",
    description = ("Simple python module to interact with Android Debug Bridge tool"),
    license = "BSD",
    keywords = "python android adb",
    url = "https://github.com/sch3m4/pyadb",
    packages=['pyadb'],
    classifiers=[
        "Development Status :: 4 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
