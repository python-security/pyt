from setuptools import find_packages, setup

long_description = """"""

setup(
        name='pyt',
        version='1.0.0a6',
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
            'Programming Language :: Python :: 3.4'
        ],
        keywords='security vulnerability web flask django pyt static analysis',
        packages=find_packages(exclude=['example',
                                        'profiling',
                                        'scan_results',
                                        'tests']),
        entry_points={
            'console_scripts': [
                'pyt = pyt.pyt:main'
            ]
        }
)
