from setuptools import setup, find_packages

setup(
    name="pyspark_recommendation_system",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pyspark",
    ],
    description="Recommendation systems using pyspark",
    authors=["Gaurab Subedi", "Siddhi Kiran Bajracharya", "Unish Rajkarnikar"],
)
