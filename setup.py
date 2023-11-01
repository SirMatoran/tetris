from setuptools import setup

setup(
    name="Tetris by Alexis Bianchi",
    version="1.0.0.dev",
    packages=["src"],
    entry_points={"console_scripts": ["tetris=src.main:main"]},
    description="Python Tetris Game",
    author="Alexis Bianchi",
    author_email="alexisbianchi18@icloud.com",
)
