import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ukrainealarm",
    use_scm_version=True,
    author="Pavlo Annekov",
    author_email="paul.annekov@gmail.com",
    description="Implements api.ukrainealarm.com API that returns info about Ukraine air raid alarms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/PaulAnnekov/ukrainealarm",
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'aiohttp>=3.8.1'
    ],
    setup_requires=[
        'setuptools_scm'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
