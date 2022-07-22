from setuptools import setup, find_packages

with open("./src/pykvs/__init__.py") as f:
    exec(f.read())

setup(
    name="pykvs",
    version=__version__,
    url="https://github.com/kujirahand/pykvs",
    author="kujirahand",
    author_email="web@kujirahand.com",
    maintainer="kujirahand",
    maintainer_email="web@kujirahand.com",
    description="Simple and convenient Key-value Store Library",
    packages=find_packages(where='src'),
    install_requires=[],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
