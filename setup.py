try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='rkm_codes',
    version='0.5.0',
    description='QuantiPhy support for RKM codes.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author="Ken Kundert",
    author_email='rkm_codes@nurdletech.com',
    packages='rkm_codes'.split(),
    url='https://nurdletech.com/linux-utilities/rkm_codes',
    download_url='https://github.com/kenkundert/rkm_codes/tarball/master',
    license='GPLv3+',
    zip_safe=True,
    install_requires='quantiphy>=2.4'.split(),
    setup_requires='pytest-runner>=2.0'.split(),
    tests_require='pytest'.split(),
    keywords=[
        'rkm codes',
        'quantiphy',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        #'Programming Language :: Python :: 3.3',
        #    should work, but is no longer tested
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
)
