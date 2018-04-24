from setuptools import find_packages
from setuptools import setup


VERSION = '0.34'


setup(
    name='python-taint',
    packages=find_packages(exclude=(['tests*'])),
    version=VERSION,
    include_package_data=True,
    description='Find security vulnerabilities in Python web applications'
    ' using static analysis.',
    long_description="Check out PyT on `GitHub <https://github.com/python-security/pyt>`_!",
    url='https://github.com/python-security/pyt',
    author='python-security',
    author_email='mr.thalmann@gmail.com',
    download_url='https://github.com/python-security/pyt/archive/{}.tar.gz'.format(VERSION),
    license='GPLv2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Security',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=['security', 'vulnerability', 'web', 'flask', 'django', 'static-analysis', 'program-analysis'],
    install_requires=[
        'graphviz>=0.4.10',
        'requests>=2.12',
        'GitPython>=2.0.8'
    ],
    entry_points={
        'console_scripts': [
            'pyt = pyt:main'
        ]
    }
)
