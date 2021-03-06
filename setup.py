from setuptools import setup, find_packages

# # This was done at install time, I did it once and pushed it until there's no documentation
# from compiler.proto import compile
# compile()

with open("requirements.txt") as f:
	requirements = f.read().split("\n")

setup(
	name='aiocraft',
	version='0.0.7',
	description='asyncio-powered headless minecraft client library',
	url='https://github.com/alemidev/aiocraft',
	author='alemi',
	author_email='me@alemi.dev',
	license='MIT',
	packages=find_packages(),
	package_data = {
		'aiocraft': ['py.typed'],
	},
	install_requires=requirements,
	classifiers=[
		'Development Status :: 1 - Planning',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',  
		'Operating System :: POSIX :: Linux',		 
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.8',
	],
)
