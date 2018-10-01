from distutils.core import setup
setup(
	name="ip_checker",
	version="1.0",
	author = "Bisrat Yalew",
	author_email="bisratyalew10@gmail.com",
	packages=["ip_checker"],
	scripts=[],
	url='http://pypi.python.org/pypi/py_ip_checker',
	license="LICENSE.txt",
	description="check if ip address is valid, public or private"
	long_description=open('README.md').read(),
	install_requires=[],)