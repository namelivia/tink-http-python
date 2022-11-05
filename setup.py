from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="tink-http-python",
    version="0.0.2",
    description="Python SDK for accessing the tink API ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/namelivia/tink-http-python",
    author="José Ignacio Amelivia Santiago",
    author_email="jignacio.amelivia@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="tink, api",
    python_requires=">=3.8, <4",
    install_requires=[
        "tink-python-api-types",
        "requests",
        "requests-oauthlib",
        "pyhumps",
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    project_urls={
        "Bug Reports": "https://github.com/namelivia/tink-http-python/issues",
    },
)
