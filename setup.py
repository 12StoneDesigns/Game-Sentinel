from setuptools import setup, find_packages

setup(
    name="game-sentinel",
    version="0.1.0",
    author="T. Landone Love",
    author_email="12stonedesigns@gmail.com",
    description="A sophisticated game testing framework for RPG mechanics",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/12stonedesigns/game-sentinel",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Testing",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    include_package_data=True,
)
