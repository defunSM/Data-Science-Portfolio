from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version='0.1.0',
    description='Using Machine Learning Techniques to forecast future commodity prices in Eve Online in order to create recommendations on which commodities are most profitable.',
    author='Salman Hossain',
    license='MIT',
)
