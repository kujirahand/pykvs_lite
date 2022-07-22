from setuptools import setup, find_packages
from pykvs_lite import __version__ # バージョン情報取得のため

# get readme
with open("./README.md") as f:
    # long_desc = f.read().split("## Sample\n")[0]
    long_desc = f.read()

AUTHOR = 'kujirahand'
EMAIL = 'web@kujirahand.com'

# setup
setup(
    name="pykvs_lite",
    url="https://github.com/kujirahand/pykvs_lite",
    description="Simple and convenient Key-value Store Library",
    author=AUTHOR,
    author_email=EMAIL,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    version=__version__,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=[],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
