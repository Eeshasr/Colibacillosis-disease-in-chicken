

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="CNNCLASIFIER",
    version="0.0.0",
    author="Eeshasr",
    author_email="eesharavindran@gmail.com",
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eeshasr/Colibacillosis-disease-in-chicken",
    project_urls={
        "Bug Tracker": "https://github.com/Eeshasr/Colibacillosis-disease-in-chicken/issues",
    },
    package_dir={"": "src()"},
    packages=setuptools.find_packages(where="src()"))