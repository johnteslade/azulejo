from setuptools import setup


#see http://pypi.python.org/pypi/stdeb for package building instructions
#or else here: https://github.com/astraw/stdeb

setup(name='azulejo',
      version='0.1',
      author='Pedro',
      author_email='pedro@lamehacks.net',
      packages=['azulejo'],
      include_package_data=True,
      scripts=['bin/azulejo'],
      )
