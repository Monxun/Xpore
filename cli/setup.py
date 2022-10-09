from importlib_metadata import entry_points
from setuptools import setup, version, find_packages

setup(
    name='xpore',
    version='0.1.0',
    author='CycleDelic Team',
    packages=find_packages(),
    install_requires=[
        'click',
        'importlib_metadata',
        'jinja2',
        'pyyaml',
        'hydra-core',
        'python-dotenv',
        'kaggle'
    ],
    entry_points='''
    [console_scripts]
    xpore=xpore:cli
    '''
)