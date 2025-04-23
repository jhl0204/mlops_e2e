from setuptools import find_packages, setup
from typing import List

HYPEHN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    function will return the list of requirements
    '''
    requiremens = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace('\n', '') for r in requirements]

        if HYPEHN_E_DOT in requirements:    
            requirements.remove(HYPEHN_E_DOT)

    return requirements

setup(
    name ='mlops_endtoend',
    version='0.0.1',
    author='JHL',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)