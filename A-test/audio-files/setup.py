import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = 'audio',
	version = '0.1',
	scripts = ['init'],
	author= 'Joseph Dittrick',
	author_email= "josephdittrick@gmail.com",
	description = 'Package originally made to do tests for a vocal assistant',
	long_description = long_description,
	long_description_type= "text/markdown",
	packages = setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: Qwant prototype :: Qwant License ?",
		"Operating System :: OS Independant",
	],
)