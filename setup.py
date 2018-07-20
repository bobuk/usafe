from setuptools import setup, find_packages
setup(name="usafe", version="0.1.0",
      py_modules=['usafe'],
      url="http://github.com/bobuk/usafe",
      author="Grigory Bakunov",
      author_email='thebobuk@ya.ru',
      description='oversimplistic secret data storage with cryptography protection',
      install_requires=[
          'privy'
      ],
      scripts = ['scripts/usafe-archive'],
      classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],

)
