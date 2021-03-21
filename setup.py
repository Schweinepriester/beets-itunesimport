from setuptools import setup

setup(
    name='beets-itunesimport',
    version='0.1.0.dev0',  # TODO
    description='',  # TODO
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Kai Hollberg',
    author_email='kai.hollberg@gmail.com',
    url='https://github.com/Schweinepriester/beets-itunesimport',
    license='MIT',
    platforms='WIN',  # TODO

    packages=['beetsplug'],

    python_requires='>=3.7',
    install_requires=[
        'beets>=1.4.9',
    ],

    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
    ],
)
