from distutils.core import setup
import setuptools

setup(
    name="FlaskRequestLogging", # Replace with your own username
    packages = ['FlaskRequestLogging'],
    version="0.0.2",
    license='MIT',
    description="A middleware to log all information of header and payload of response and request",
    author="vinhvungoc",
    author_email="vinhvungoc@vccorp.vn",
    url="https://github.com/ngocvinhvu/logging_middleware.git",
    download_url="",
    keywords=["LOGGING", "FLASK", "PYTHON"],
    install_requires=[
        "logging",
        "flask",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
