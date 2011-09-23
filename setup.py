try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='Blogy',
    version='0.1-dev',
    url='http://blog.apolloner.eu',
    license='BSD',
    author='Florian Apolloner',
    author_email='florian@apolloner.eu',
    description='Simple blogging engine',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=['blogy', 'blogy.utils'],
    package_data={'blogy': ['static/*', 'templates/*']},
    platforms='any'
)
