from setuptools import setup


requires = [
    'behave',    # For testing features
    'requests',  # For testing HTTP API calls
    'oktest',    # For testing units
    'falcon',    # REST framework
    'cython',    # For accelerating falcon (optional)
]

setup(
    name='Ticketing System',
    install_requires=requires,
)
