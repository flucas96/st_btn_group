import setuptools


with open('README.md') as f:
    long_desc = f.read()

setuptools.setup(
    name="st_btn_group",
    version="0.0.11",
    author="",
    author_email="",
    setup_requires=['wheel'],
    license='MIT',
    description="Streamlit Component for BaseWeb Button Group",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)

