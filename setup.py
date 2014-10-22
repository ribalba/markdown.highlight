from distutils.core import setup

setup(
    name='MarkdownHighlight',
    version='0.1.3',
    packages=['MarkdownHighlight',],
    license='Apache License 2.0',
    long_description=open('README.txt').read(),
    url='https://github.com/ribalba/markdown.highlight',
    description='A markdown extension that enables you to create <mark> tag by using ???some text???',
    author='Didi Hoffmann',
    author_email='didi@ribalba.de',
    install_requires=[
        "Markdown >= 2.3.1",
    ],
)