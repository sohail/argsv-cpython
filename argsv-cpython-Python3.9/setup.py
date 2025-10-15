from setuptools import setup, Extension

module = Extension('argsv',
                   sources=['src/argsv.c'],  # Adjust if lib/cbow.cpp not used
                   include_dirs=['F:/cpython/Include', './src/'],
                   library_dirs=['F:/cpython/PCbuild/amd64', 'F:/CBOW/'],
                   libraries=['python315'],  # Remove 'cbow' if source included
                   extra_compile_args=['/EHsc', '/MD'],
                   extra_link_args=['/LIBPATH:F:/cpython/PCbuild/amd64'])

setup(
    name='argsv',
    version='0.1.0',
    description='Command line argument processor.',
    long_description=open('./README.md').read(),  # Optional, for PyPI
    long_description_content_type='text/markdown',  # If using README.md
    author='Q@khaa.pk',
    author_email='Q@khaa.pk',  # Optional
    url='https://github.com/sohail/argsv-cpython.git',  # Optional
    license='khaa.pk Non-Commercial License',  # Custom license name
    package_data={'cbow': ['lib/cbow.h', 'LICENSE']},  # Include LICENSE
    install_requires=[''],  # Remove if not needed
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.15',
        'License :: Other/Proprietary License',  # For custom licenses
        'Operating System :: Microsoft :: Windows'
    ],
    ext_modules=[module]
)
