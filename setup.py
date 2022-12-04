from setuptools import setup

setup(
	name='snowflake',
	version='0.1.0',
	description='A example Python package',
	url='https://github.com/khsazz/dsss-snowflake-assignement',
	author='Khaled Hasan Sazzad',
	author_email='khaledhasansazzad@gmail.com',
	license='Apache 2.0',
	packages=['snowflake'],
	install_requires=['numpy~=1.21.5',
					  'turtles']
)
