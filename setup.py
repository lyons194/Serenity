#setup.py

setup(
    name="web_scraper",
    version="1.0.0",
    description="A GUI-based web scraper",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lyons194",
    author="Sean Lyons",
    author_email="slyons494@gmail.com",
    license="GNU General Public License v3.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Programming Lanuage :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["web_scraper"],
    include_package_date=True,
    install_reqires=["requests","beautifulsoup4"
    ]
    entry_points={"web_scraper": ["web_scraper.__main__:main"]},
)
