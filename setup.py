### encoding: utf-8 ###

"""
Flask-AYAH
-------------

Are You a Human? Flask Extension
"""
from setuptools import setup


setup(
    name='Flask-AYAH',
    version='0.1',
    url='http://github.com/Chekosoft/flask-ayah',
    license='BSD',
    author=u'Joaquín Muñoz M.',
    author_email=u'jemunozmunoz@gmail.com',
    description='Are you a Human? Flask Extension',
    long_description=__doc__,
    py_modules=['flask_ayah'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'are-you-a-human'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)