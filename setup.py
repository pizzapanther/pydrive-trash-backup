import setuptools

setuptools.setup(
    name="trashpy",
    version="1.0.0",
    author="Paul Bailey",
    author_email="paul.m.bailey@gmail.com",
    description="Download your Google Drive Trash folder",
    long_description="Download your Google Drive Trash folder",
    long_description_content_type="text/markdown",
    url="https://github.com/pizzapanther/pydrive-trash-backup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['google-api-python-client', 'google-auth-oauthlib'],
)