from setuptools import setup, find_packages
from pathlib import Path


def read(filename: str):
    with open(Path(__file__).parent / filename, mode='r', encoding='utf-8') as f:
        return f.read()


def get_version() -> str:
    local_dict = {}
    with open(str(Path(__file__).parent / 'torch_crystals' / '__version.py'), 'r') as f:
        exec(f.read(), {}, local_dict)

    return local_dict['__version__']


__version__ = get_version()

with open('requirements.txt') as req_file:
    install_requires = req_file.read().splitlines()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]

setup(
    name='torch_crystals',
    packages=find_packages(),
    version=__version__,
    author='Vladimir Starostin',
    author_email='vladimir.starostin@uni-tuebingen.de',
    description='Fast PyTorch-accelerated simulation of the diffraction patterns.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    python_requires='>=3.6',
    install_requires=install_requires,
    classifiers=classifiers,
)
