from setuptools import setup, find_packages


# Parse the version from the mapbox module.
with open('taigacli/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue

setup(name='taigacli',
      version=version,
      description="Command line interface to Taiga",
      classifiers=[],
      keywords='',
      author="Alksey Cherepanov",
      author_email='ftp27host@gmail.com',
      url='https://github.com/Indev-Group/taiga_cli',
      license='MIT',
      packages=[
          'taigacli',
      ],
      package_dir={'taigacli':
                   'taigacli'},
      install_requires=[
          'terminaltables',
          'python-taiga',
          'click',
          'click-plugins'],
      entry_points={
          'console_scripts': [
              'taigacli=taigacli.cli:cli'
          ]
      },
)
