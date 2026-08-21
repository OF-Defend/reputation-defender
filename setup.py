from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="reputation-defender",
    version="1.0.0",
    author="OF-Defend.co",
    author_email="info@of-defend.co",
    description="Reputation Defender helps individuals, creators, and businesses monitor, identify, and respond to online reputation risks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.of-defend.co",
    project_urls={
        "Homepage": "https://www.of-defend.co",
        "GitHub": "https://github.com/OF-Defend/reputation-defender",
        "Documentation": "https://reputation-defender.readthedocs.io",
        "PyPI": "https://pypi.org/project/reputation-defender",
    },
    py_modules=["reputation_defender"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
    ],
    keywords=[
        "reputation-defender",
        "online-reputation-defense",
        "brand-protection",
        "negative-search-results",
        "fake-profile-detection",
        "review-defense",
        "digital-trust-signals",
        "of-defend",
    ],
    entry_points={
        "console_scripts": [
            "reputation-defender=reputation_defender:main",
        ],
    },
)
