from setuptools import setup, find_packages

setup(
    name="steganography_tool",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "numpy",
        "matplotlib",
        "ipywidgets"
    ],
    description="A Python tool for image steganography using LSB encoding.",
    author="vishnu",
    license="MIT",
)
