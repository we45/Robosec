from distutils.core import setup

install_dependencies = (
    'requests == 2.8.14',
    'dnspython == 1.15.0',
    'argparse == 1.4.0'
    'robotframework==3.0.2'
)


setup(
    name='Robot2sublist3r',
    version='0.1',
    packages=['','subbrute'],
    package_dir={'': 'Robot2sublist3r'},
    package_data={'subbrute':['*']},
    url='',
    license='MIT License',
    author='Umar Farook',
    author_email='Twitter: @umarfarook882',
    description='Robot Framework Automation for Sublist3r(Sub Domain Enumeration'
)