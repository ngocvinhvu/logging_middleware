from distutils.core import setup

setup(
    name="FlaskRequestLogging", # Replace with your own username
    packages = ['FlaskRequestLogging'],
    version="0.1",
    license='MIT',
    description="A middleware to log all information of header and payload of response and request",
    author="vinhvungoc",
    author_email="vinhvungoc@vccorp.vn",
    url="https://github.com/ngocvinhvu/logging_middleware.git",
    download_url="https://github.com/ngocvinhvu/logging_middleware/archive/refs/tags/v0.1.tar.gz",
    keywords=["LOGGING", "FLASK", "PYTHON"],
    install_requires=[
        "logging",
        "flask",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
