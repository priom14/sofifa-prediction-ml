from setuptools import find_packages, setup
import os
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirments(path: str) -> List:
    
    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirment.replace('\n','') for requirment in requirements]
    
    if HYPHEN_E_DOT in requirements:
        del HYPHEN_E_DOT
    
        return requirements
        
        
setup(
    name= "Sofifa mrkt value prediction",
    version= "0.0.1",
    description="This is a simple sofifa ml project",
    author= "Priom Pal",
    author_email="priompalnfs@yahoo.com",
    packages= find_packages(),
    install_requires = get_requirments('requirments.txt')
)