import os
from setuptools   import setup, find_packages, Extension
from pip.req      import parse_requirements
from pip.download import PipSession


# import the data inside package/info.py file, without trigger the
#  importing of the whole package.
#  equivalent to the python2 execfile routine.
SRC_DIR = 'gerobust'
INFO_FILE = SRC_DIR + '/info.py'
with open(INFO_FILE) as fd:
    code = compile(fd.read(), INFO_FILE, 'exec')
    local_vars = {}
    exec(code, {}, local_vars)  # don't use global vars, save local_vars
    __pkg_name__ = local_vars['PACKAGE_NAME']  # save the interesting data
    __version__ = local_vars['PACKAGE_VERSION']


# access to the file at the package top level (like README)
def path_to(filename):
    return os.path.join(os.path.dirname(__file__), filename)

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(path_to('requirements.txt'),
                                  session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]



ext_geolib = Extension(
    SRC_DIR + '._wrapped_geolib',
    [SRC_DIR + '/geolib.c', SRC_DIR + '/geolib.i'],
    extra_compile_args = ['-O3', '-frounding-math', '-fsignaling-nans'],
    libraries=['c'],
    swig_opts=['-py3'],
)


setup(
    name=__pkg_name__,
    version=__version__,
    packages=find_packages(),
    include_package_data=True,  # read the MANIFEST.in file
    install_requires=reqs,
    zip_safe=False,

    ext_modules=[ext_geolib],

    author='lucas bourneuf',
    author_email='lucas.bourneuf@openmailbox.org',
    description='Extension in C for incircles tests (2D/3D)',
    long_description=open(path_to('README.mkd')).read(),
    keywords='C function robust geometry',
    url='https://github.com/aluriak/gerobust',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: C',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
