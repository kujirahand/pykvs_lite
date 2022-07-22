from setuptools import setup, find_packages

# get version
with open("./pykvs/version.py") as f:
    exec(f.read())

# setup
setup(
    name="pykvs",
    version=__version__,
    url="https://github.com/kujirahand/pykvs",
    author="kujirahand",
    author_email="web@kujirahand.com",
    maintainer="kujirahand",
    maintainer_email="web@kujirahand.com",
    description="Simple and convenient Key-value Store Library",
    packages=find_packages(where='.'),
    install_requires=[],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
