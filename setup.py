from setuptools import setup

long_description = None
with open('README.md') as f:
    long_description = f.read()

setup(
    name='ip_checker',
    packages=['ip_checker',],
    version='0.1',
    description='A Library that checks whether an ipaddress is valid, public or private',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bisratyalew/ip_checker',
    keywords=['valid', 'ip', 'ipaddress', 'public', 'private', 'check ip address', 'python ip address checker'],
    author='Bisrat Yalew',
    author_email='bisratyalew10@gmail.com',
    license='MIT',
    classifiers=[       
        "License :: OSI Approved :: MIT License",
        ],
)