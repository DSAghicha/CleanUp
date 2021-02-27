from setuptools import setup

setup(
    name="CleanUP",
    version=1.0,
    packages=['cleanup'],
    requires='requirements.txt',
    entry_points={
        'console_scripts': [
            'cleanup = cleanup.__main__:main'
        ]
    }
)
