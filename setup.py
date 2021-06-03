from setuptools import setup, find_packages

setup(
    name='wif',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Click',
        'google-auth',
        'google-cloud-storage',
    ],
    entry_points={
        'console_scripts': [
            'wif = wif.cli:cli',
        ],
    },
)
