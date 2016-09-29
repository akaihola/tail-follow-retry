from setuptools import setup

from tail_follow_retry import __doc__, __version__

setup(
    name='tail-follow-retry',
    version=__version__,
    author='Antti Kaihola',
    author_email='antti.kaihola@eniram.fi',
    description=__doc__.split('\n')[0],
    long_description=__doc__,
    url='https://github.com/akaihola/tail-follow-retry',
    py_modules=['tail_follow_retry'],
    license='BSD',
    zip_safe=True,
    entry_points={'console_scripts': ['tailfr = tail_follow_retry:main']},
    keywords='tail',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'])
