from setuptools import setup, find_packages
from pip.req import parse_requirements


install_reqs = parse_requirements('requirements.txt', session=False)
version = '0.0.1'
README = """Python library for generating images to attract attention in social media."""

setup(
    name='kdpv_generator',
    version=version,
    description=README,
    long_description=README,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Graphics'
    ],
    keywords='spbpython,python',
    author='Dmitry Nazarov',
    author_email='mail@nazarov.tech',
    maintainer='Dmitry Nazarov',
    packages=find_packages(),
    url='https://github.com/spbpython/kdpv_generator',
    license='MIT',
    install_requires=[str(ir.req) for ir in install_reqs],
    include_package_data=True,
    package_data={
        'kdpv_generator': ['assets/fonts/*', 'assets/images/*.png', 'configs/*.yml',
                           'tests/configs/*.yml', 'tests/images/*.png']
    },
    test_suite='pytest',
    zip_safe=True,
)
