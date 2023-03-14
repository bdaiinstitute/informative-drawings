from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# Setting up
setup(
    name="informative_drawings",
    version=0.1,
    author="carolineec (Caroline Chan)",
    author_email="<cmchan@mit.edu>",
    description="Learning to generate line drawings that convey geometry and semantics",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # install_requires=[
    #     "numpy >=1.24.1",
    #     "bosdyn-client >=3.2.1.post1",
    #     "bosdyn-api >=3.2.1.post1",
    #     "drake >= 1.11.0",
    #     "torch >= 1.13.1",
    #     "torchvision >= 0.14.1",
    #     "pillow >= 9.0.1",
    #     "openai >= 0.26.0",
    #     "opencv-python >= 4.7.0.68",
    # ],
)
