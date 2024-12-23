from setuptools import setup, find_packages

setup(
    name='demo_tts',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'coqui-ai-tts',
    ],
    entry_points={
        'console_scripts': [
            'demo_tts=main:main',
        ],
    },
)
