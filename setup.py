''' Setup Tool '''
import sys
from setuptools import setup, find_packages
__version__ = '0.0.1'
__package_name__ = 'deeploy'

with open('README.md') as doc:
    __long_description__ = doc.read()

if sys.version_info < (3, 0):
    raise Exception(f'Python 3.0 or above is required to run {__package_name__}')


setup(
    name=__package_name__,
    version=__version__,
    author='Ukor Jidechi Ekundayo',
    author_email='ukorjidechi@gmail.com',
    description='A deployment script',
    long_description=__long_description__,
    keyword=['Delopy', 'Deployment', 'Deeploy', 'CI/CD', 'DevOps'],
    license='MIT',
    url='https://github.com/ukor/deeploy',
    packages=find_packages(exclude=['__tests', 'tests', '*.tests', '*.tests.*', 'tests.*']),
    python_requires='>=3.0.*',
    install_requires=['falcon', 'gunicorn'],
    extras_require={
        'dev': [
            'pytest', 'coverage', 'pytest-cov', 'pylint', 'codecov', 'python-coveralls'
        ]
    },
    project_urls={
        'Documentation': 'https://github.com/ukor/deeploy/blob/master/README.md',
        'Changelog': '',
        'Issue Tracker': 'https://github.com/ukor/deeploy/issues',
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software :: Dev Ops',
        'Topic :: Software Developemt :: CD',
        'Topic :: Software Development :: Deployment',
    ],
)
