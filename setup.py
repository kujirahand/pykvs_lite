from setuptools import setup, find_packages

# get version
with open("./pykvs_lite/version.py") as f:
    exec(f.read())

# get readme
with open("./README.md") as f:
    long_desc = f.read().split("## Sample\n")[0]

# setup
setup(
    name="pykvs_lite",
    version=__version__,
    url="https://github.com/kujirahand/pykvs",
    author="kujirahand",
    author_email="web@kujirahand.com",
    maintainer="kujirahand",
    maintainer_email="web@kujirahand.com",
    description="Simple and convenient Key-value Store Library",
    packages=find_packages(where='.'),
    install_requires=[],
    long_description=long_desc,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
