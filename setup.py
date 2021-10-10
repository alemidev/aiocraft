from setuptools import setup, find_packages

setup(
	name='aiocraft',
	version='0.0.1',	
	description='asyncio-powered headless minecraft client',
	url='https://github.com/alemidev/aiocraft',
	author='alemi',
	author_email='me@alemi.dev',
	license='MIT',
	packages=find_packages(),
	install_requires=['requests'],
	classifiers=[
		'Development Status :: 1 - Planning',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',  
		'Operating System :: POSIX :: Linux',		 
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.8',
	],
)

