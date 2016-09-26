from setuptools import setup, find_packages
import os

version = __import__('text_ckeditor').__version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

DESCRIPTION = 'Django CMS plugin collection'

setup(
    name="django-cms-plugins",
    version=version,
    url='http://github.com/rouxcode/django-cms-plugins',
    license='MIT',
    platforms=['OS Independent'],
    description=DESCRIPTION,
    long_description=read('README.rst'),
    author=u'Alaric Maegerle',
    author_email='info@rouxcode.ch',
    packages=find_packages(),
    install_requires=(
        'cssselect>=0.9.2',
        'Django>=1.8,<1.10',
        'django-cms>=3.3.2,<3.5',
        'django-filer>=1.2.0,<1.3',
        'google>=2.4.4',
        'lxml>=3.6.4',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)