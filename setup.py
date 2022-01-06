"""Setup file for the library."""
from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent

README = (HERE / "readme.md").read_text()

URL = "https://github.com/ZER0-X/python-telegram2rss"
ISSUES = "https://github.com/ZER0-X/python-telegram2rss/issues"
CHANGELOG = "https://github.com/ZER0-X/python-telegram2rss/blob/main/CHANGELOG.md"


VERSION = '0.1.0'

DESCRIPTION = "A python library to fetch data from public Telegram channels to use them as a python object or RSS feed."


setup(
    name="telegram2rss",
    version=VERSION,
    author="zer0-x",
    license="GPL-3.0",
    url=URL,
    project_urls={
        "Issues": ISSUES,
        "Changelog": CHANGELOG,
    },
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=README,
    packages=find_packages(),
    install_requires=[""],
    tests_require=["pytest"],
    test_suite="tests",
    keywords=["Python", "Telegram", "RSS"]
)