from setuptools import setup, find_namespace_packages


setup(
    name='rrna-16s-analysis-service',
    version='0.1.0-alpha',
    packages=find_namespace_packages(),
    entry_points={},
    scripts=[],
    package_data={
    },
    install_requires=[
        'fastapi',
        'uvicorn',
        'sqlalchemy',
        'alembic',
    ],
    description='16S rRNA analysis service',
    url='https://github.com/BCCDC-PHL/rrna-16s-analysis-service',
    author='Dan Fornika',
    author_email='dan.fornika@bccdc.ca',
    include_package_data=True,
    keywords=[],
    zip_safe=False
)
