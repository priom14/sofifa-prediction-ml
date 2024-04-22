from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    
    return requirements
setup(
    name= "Sofifa mrkt value prediction",
    version= "0.0.1",
    description="This is a simple sofifa ml project",
    author= "Priom Pal",
    author_email="priompalnfs@yahoo.com",
    packages= find_packages(),
    install_requires = get_requirements('requirments.txt')
)