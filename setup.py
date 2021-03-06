import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FlaskRequestLogging", # Replace with your own username
    version="0.0.2",
    author="Rose",
    author_email="vinhvungoc@vccorp.vn",
    description="A middleware to logging request and response",
    long_description=long_description,
    long_description_content_type="",
    url="https://github.com/ngocvinhvu/logging_middleware.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
