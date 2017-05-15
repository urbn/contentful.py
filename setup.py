from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

version_ns = {}
with open('contentful/cda/version.py') as f:
    exec(f.read(), version_ns)


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]
    default_args = ['test/']

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        args = self.pytest_args
        if isinstance(args, str):
            args = args.split()
        errno = pytest.main(self.default_args + args)
        sys.exit(errno)

deps = [
    'requests==2.4.3',
    'six==1.10.0',
    'python-dateutil>=2.3'
]

if sys.version_info < (3, 5):
    deps.append('enum34==1.1.1')

test_deps = [
    'mock',
    'vcrpy==1.7.4',
    'pytest==2.6.4'
]

with open('README.rst') as f:
    readme = f.read()

setup(
    name='contentful.py',
    version=version_ns['__version__'],
    packages=['contentful', 'contentful.cda'],
    url='https://github.com/contentful-labs/contentful.py',
    license='Apache 2.0',
    author='Contentful GmbH',
    author_email='python@contentful.com',
    description='Python SDK for Contentful\'s Content Delivery API',
    long_description=readme,
    install_requires=deps,
    tests_require=test_deps,
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
