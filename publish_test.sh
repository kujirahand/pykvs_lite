#!/bin/bash
rm -f -r dist
rm -f -r build
rm -f -r pykvs_lite.egg-info

python3 setup.py sdist
python3 setup.py bdist_wheel

twine upload --repository testpypi dist/*

