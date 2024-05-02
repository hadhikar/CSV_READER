from setuptools import setup, find_packages

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name="csv_reader",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    entry_points="""
        [console_scripts]
        csv_reader=csv_reader.app:cli
    """,
)
