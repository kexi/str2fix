from setuptools import setup

setup(
    name='str2fix',
    version='0.1.0',
    description='A example Python package',
    long_description=open('README.me').read(),
    url='https://github.com/kexi/str2fix',
    author='kexi',
    author_email='kexi@kexi.jp',
    license='MIT',
    packages=['str2fix'],
    install_requires=['mojimoji', ],
    keywords=['japanese', '固定長'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
