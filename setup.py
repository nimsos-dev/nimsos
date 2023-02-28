from setuptools import setup, find_packages

setup(
    name="nimsos",
    version="1.0.0",
    author="NIMS-OS developers",
    url="https://github.com/",
    license="MIT",
    description='NIMS-OS package',
    #packages=find_packages(where='nimsos'),
    #package_dir={'': 'nimsos'},
    packages=["nimsos", "nimsos.ai_tools", "nimsos.input_tools", "nimsos.output_tools","nimsos.visualization" ],
    install_requires=[
        "Cython",
        "matplotlib",
        "numpy",
        "physbo",
        "scikit-learn",
        "scipy"
    ]
)
