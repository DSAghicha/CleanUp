from setuptools import setup

setup(
    name="CleanUP",
    version=1.0,
    packages=['cleanup'],
    entry_points={
        'console_scripts': [
            'cleanup = cleanup.__main__:main'
        ]
    }
)
