from setuptools import setup, find_packages
import codecs
import os


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('README.md') as readme_file:
    README = readme_file.read()

with open('CHANGELOG.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='backtraderbd',
    version=read('backtraderbd/VERSION.txt'),
    description='A backtrader utility',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Raisul Islam',
    author_email='raisul.exe@gmail.com',
    keywords=['backtrader','backtester'],
    url='https://github.com/rochi88/backtraderbd',
    download_url='https://github.com/rochi88/backtraderbd/archive/master.zip'
)

install_requires = [
    'beautifulsoup4',	
    'requests', 
    'pandas',
    'backtrader',
    'bdshare',
    'arctic'
]

classifiers=[
        'Development Status :: 1 - Dev',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires, classifiers=classifiers)