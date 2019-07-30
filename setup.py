from setuptools import setup, find_packages

setup(
  name='deeploy',
  version='0.0.1',
  script=['say_hello.py'],
  author='Ukor, Jidechi Ekundayo',
  author_email='ukorjidechi@gmail.com',
  description='A minilist deployment script',
  keyword='Delopy Deployment deeploy',
  url='https://github.com/ukor/deeploy',  # project website
  packages=find_packages('deeploy'),
  python_requires='>=3.6.*',
  project_urls={
    'Documentation': '',
    'Changelog': '',
    'Issue Tracker': 'https://github.com/ukor/deeploy/issues',
  },
)
