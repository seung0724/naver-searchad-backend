from setuptools import setup, find_packages

setup(
    name="naver_searchad",
    version="0.1.0",
    description="Wrapper for Naver Search Ads API",
    author="Your Name",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "requests>=2.25.0",
        "beautifulsoup4>=4.9.0",
        "python-dotenv>=0.21.0"
    ],
    python_requires=">=3.7",
)
