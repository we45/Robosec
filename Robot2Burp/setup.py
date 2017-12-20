from distutils.core import setup

install_dependencies = (
    'requests == 2.8.14',
    'robotframework == 3.0.2',
    'bs4 == 0.0.1'
)


setup(
    name='Robot2Burp',
    version='0.1',
    packages=[''],
    package_dir={'': 'robot2burp'},
    url='',
    license='MIT License',
    author='Umar Farook',
    author_email='Twitter: @umarfarook882',
    description='Robot Framework Automation Script for Burp'
)