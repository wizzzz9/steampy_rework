from setuptools import setup
import sys

if not sys.version_info[0] == 3 and sys.version_info[1] < 8:
    sys.exit('Python < 3.8 is not supported')

version = '0.0.1'

setup(
    name='steampy_rework',
    packages=['steampy_rework', 'test', 'examples', ],
    version=version,
    description='A Steam lib for trade automation',
    author='Viacheslav Patokin',
    author_email='viacheslavpatokin@gmail.com',
    license='MIT',
    url='https://github.com/wizzzz9',
    download_url='https://github.com/wizzzz9/steampy_rework/tarball/' + version,
    keywords=['steam', 'trade', 'steamapi'],
    classifiers=[],
    install_requires=[
        "requests",
        "beautifulsoup4",
        "rsa"
    ],
)