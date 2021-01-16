from setuptools import setup, find_packages

setup(
    name = 'pytorch_serde',
    url = "https://vergeai.io/",
    author = "Vale Tolpegin",
    author_email = "valetolpegin@gmail.com",
    version = "1.0",
    maintainer = "Vale Tolpegin",
    maintainer_email = "valetolpegin@gmail.com",
    packages = find_packages(exclude = ('tests', 'doc')),
    install_requires = [
        'numpy==1.19.4',
        'torch==1.7.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Sphinx',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
