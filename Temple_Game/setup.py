try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

runner = 'runner.py'
rooms = 'rooms.py'

config = {
    'description': 'Temple_Game',
    'author': 'Michael Lennon',
    'url': 'URL to get at it',
    'download_url': 'Where to download it',
    'author_email': 'mlennon3@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Temple_Game'],
    'scripts': [runner, rooms],
    'name': 'Temple_Game'
}

setup(**config)
