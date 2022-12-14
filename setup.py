from setuptools import setup

setup(
    name='flakstore',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'gunicorn',
        'flask-wtf',
        'flask-bcrypt',
        'wtforms[email]',
        'Flask-Login'
    ],
)