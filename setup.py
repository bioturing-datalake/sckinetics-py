import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sckinetics",
    version="1.0",
    author="bioturing",
    author_email="info@bioturing.com",
    description="scKINETICS (Key regulatory Interaction NETwork for Inferring Cell Speed)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bioturing-datalake/sckinetics-py",
    project_urls={
        "Bug Tracker": "https://github.com/bioturing-datalake/sckinetics-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7"
)
