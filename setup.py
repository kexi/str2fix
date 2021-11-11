from setuptools import setup

setup(
    name='str2fix',
    version='0.1.0',
    description='日本語文字列を固定長に変換するライブラリ',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
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
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
