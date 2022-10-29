import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lm_plot",
    version="0.1.0",
    author="Igor Ostrovsky",
    author_email="igoros@gmail.com",
    description="A tool for visualizing Language Model Evaluation Harness results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/igor0/lm-eval-plot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["pandas", "seaborn"],
    dependency_links=[],
)
