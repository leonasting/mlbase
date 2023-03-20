# Date: 2023-03-19
from setuptools import find_packages,setup# To packages are automatically detected
from typing import List# To type hinting

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Alavi',
author_email='alavi.khan@sjsu.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
