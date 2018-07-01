from setuptools import find_packages, setup

dependencies = ['click', 'python-resize-image']

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name='pig-py',
  version='0.0.1',
  author="Francisco Junior",
  author_email="fcojunr@gmail.com",
  description="A package for generate icons for Ionic",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/FcoJunior/pig-py",
  packages=find_packages(),
  include_package_data=True,
  zip_safe=False,
  platforms='any',
  install_requires=dependencies,
  data_files=[('pig/dimensions', [
    'pig/dimensions/ionic.dim.json'
  ])],
  entry_points={
    'console_scripts': [
      'pig = pig.cli:main',
    ],
  },
  classifiers=[
    # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    # 'Development Status :: 1 - Planning',
    # 'Development Status :: 2 - Pre-Alpha',
    # 'Development Status :: 3 - Alpha',
    'Development Status :: 4 - Beta',
    # 'Development Status :: 5 - Production/Stable',
    # 'Development Status :: 6 - Mature',
    # 'Development Status :: 7 - Inactive',
    # 'Environment :: Console',
    # 'Intended Audience :: Developers',
    # 'License :: OSI Approved :: BSD License',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Operating System :: MacOS',
    'Operating System :: Unix',
    'Operating System :: Microsoft :: Windows',
    # 'Programming Language :: Python',
    # 'Programming Language :: Python :: 2',
    # 'Programming Language :: Python :: 3',
    # 'Topic :: Software Development :: Libraries :: Python Modules',
  ]
)