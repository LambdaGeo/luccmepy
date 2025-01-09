from setuptools import setup, find_packages

setup(
    name="luccmepy",
    version="0.1.0",
    author="Seu Nome",
    description="Descrição breve da biblioteca",
    long_description=open("readme.md").read(),
    packages=find_packages(),
    install_requires=["numpy>=1.25.0"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
