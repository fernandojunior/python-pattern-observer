from setuptools import setup

# Read the README file
with open("README.rst") as f:
    README = f.read()

setup(
    author='Fernando Felix do Nascimento Junior',
    author_email='fernandojr.ifcg@live.com',
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    description='A observer pattern implementation in Python based on jQuery.',
    keywords='observer design pattern',
    license='MIT License',
    long_description=README,
    name='pattern-observer',
    py_modules=['observer'],
    platforms='any',
    url='https://github.com/fernandojunior/python-pattern-observer',
    version='1.0.0',
    zip_safe=False
)
