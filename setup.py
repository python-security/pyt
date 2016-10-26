from setuptools import setup, find_packages

long_description = """

"""

setup(
        name='pyt',
        version='1.0.0al',
        description='Find security vulnerabilities in Python web applications'
        ' using static analysis.',
        long_description=long_description,
        url='github url',
        author='PyT',
        author_email='mr.thalmann@gmail.com',
        license='GPLv2',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers :: Research :: Web',
            'Topic :: Security :: Research :: Web Tools :: Build Tools',
            'License :: OSI Approved :: GPLv2',
            'Programming Language :: Python :: 3.4'
        ],
        keywords='security vulnerability web flask django pyt static analysis',
        packages=find_packages(exclude=['example',
                                        'profiling',
                                        'scan_results',
                                        'tests']),
        install_requires=[]
)
