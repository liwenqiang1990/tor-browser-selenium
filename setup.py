from setuptools import setup


setup(
    name="tbselenium",
    description="Tor Browser automation with Selenium",
    keywords=["tor", "selenium", "tor browser"],
    version="0.4.2",
    url = 'https://github.com/s0irrlor7m/tor-browser-selenium',
    packages=["tbselenium", "tbselenium.test"],
    install_requires=[
        "selenium>=3.11"
    ]
)
