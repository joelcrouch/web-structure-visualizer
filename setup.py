from setuptools import setup, find_packages

setup(
    name="web-structure-visualizer",             # Library name
    version="0.1.0",                # Version
    author="Joel Crouch",             # Your name
    author_email="joelcrouch@gmail.com", # Your email
    description="A library for scraping and visualizing webpage structures.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/joelcrouch/web-structure-visualizer",  # GitHub repo (optional)
    packages=find_packages(),       # Automatically finds `web_scraper` package
    install_requires=[              # Dependencies
        "beautifulsoup4",
        "selenium",
        "requests"
    ],
    classifiers=[                   # Optional metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",        # Python version requirement
)
