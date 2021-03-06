from setuptools import setup, find_packages
import textwrap

try:
    import buildutils
except ImportError:
    pass

NAME = 'Louie'
DESCRIPTION = 'Signal dispatching mechanism'
VERSION = '1.2a1'

setup(
    name=NAME,

    version=VERSION,

    description=DESCRIPTION,

    long_description=textwrap.dedent("""
    Louie provides Python programmers with a straightforward way to dispatch
    signals between objects in a wide variety of contexts. It is based on
    PyDispatcher_, which in turn was based on a highly-rated recipe_ in the
    Python Cookbook.

    You can also get the `latest development version
    <http://getschevo.org/hg/repos.cgi/louie-dev/archive/tip.tar.gz#egg=Louie-dev>`__.

    .. _PyDispatcher: http://pydispatcher.sf.net/

    .. _recipe: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/87056
    """),

    classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='',

    author="Patrick K. O'Brien and contributors",

    author_email='louie-users@lists.berlios.de',

    url='http://louie.berlios.de/',

    download_url='http://cheeseshop.python.org/pypi/Louie',

    license='BSD',

    packages=find_packages(exclude=['doc', 'ez_setup', 'examples', 'tests']),

    zip_safe=False,

    package_data={
    # -*- package_data: -*-
    },

    test_suite = 'nose.collector',

    use_2to3=True)
      
