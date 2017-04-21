from setuptools import setup

long_description = """"""

setup(
    name='pyt',
    version='1.0.0a20 ',
    description='Find security vulnerabilities in Python web applications'
    ' using static analysis.',
    long_description=long_description,
    url='https://github.com/python-security/pyt',
    author='python-security',
    author_email='mr.thalmann@gmail.com',
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
        'Programming Language :: Python :: 3.5'
    ],
    keywords='security vulnerability web flask django pyt static analysis',
    packages=[
        'pyt'
    ],
    install_requires=[
        'graphviz==0.4.10',
        'requests==2.10.0',
        'GitPython==2.0.8'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pyt = pyt:main'
        ]
    }
)
