from setuptools import setup, find_packages

setup(
    name="echocmdlib",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'colorama',
        'termcolor',
        'pyfiglet',
        "rich"
    ],
    description="A simple and beautiful command-line interactive library, something is come from rich but more easy "
                "to use",
    author="Timothy Wu",
    author_email="wuxiaoyu1107g@gmail.com",
    url="https://github.com/yourusername/mycmdlib",  # 可选
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
