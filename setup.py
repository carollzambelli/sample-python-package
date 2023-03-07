from setuptools import setup
import os

setup(
    name='my_package',
    version='0.1',
    description='A sample Python package',
    author='Carolina Kamada',
    author_email='carolina.kamada@faculdadeimpacta.com.br',
    packages=['my_package'],
    include_package_data=True,
    install_requires=["scikit-learn==1.2.1"]
)
