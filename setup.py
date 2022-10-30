from setuptools import setup

setup(
    name='npyvi',
    version='0.1.0',
    url='https://github.com/huwcheston/npyvi',
    description='Calculates normalised pairwise variability index (nPVI), as defined in Grabe & Low (2002)',
    long_description=open('README.txt').read(),
    author='Huw Cheston',
    author_email='hwc31@cam.ac.uk',
    license='MIT',
    packages=['nPyVI'],
    python_requires='>=3',
    
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
)
