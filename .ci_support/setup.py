from setuptools import setup, find_packages

with open("../disableautomerge.txt", "r") as f:
    disable_lst = f.readlines()

with open("../requirements.txt", "r") as f:
    install_requires = []
    for l in f.readlines():
        skip = False
        for disable in disable_lst:
            if len(disable.rstrip()) > 0 and l.startswith(disable.rstrip() + "=="):
                skip = True
                break
        if not skip:
            install_requires.append(l)

setup(
    name='MetaPackage',
    packages=find_packages(exclude=['*.py']),
    install_requires=install_requires,
)
