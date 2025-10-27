from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agentic-ai",
    version="0.1.0",
    author="AgenticAI Contributors",
    description="A framework for building autonomous AI agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adityarats/AgenticAI",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "anthropic>=0.7.0",
        "langchain>=0.1.0",
        "langchain-community>=0.0.10",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "requests>=2.31.0",
    ],
)
