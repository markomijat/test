from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='rzbd2i1',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Test pour les paquets python - D2i",
    author="Marko MIJATOVIC",
    author_email='marrkonni@yahoo.com',
    url='https://github.com/markomijat/rzbd2i1',
    packages=['rzbd2i1p'],
    entry_points={
        'console_scripts': [
            'rzbd2i1p=rzbd2i1p.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='rzbd2i1',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
