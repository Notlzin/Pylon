from setuptools import setup, Extension
from Cython.Build import cythonize
import os

here = os.path.dirname(__file__)  # outer root folder
package_dir = os.path.join(here, "pylon2d")  # inner package folder

ext_modules = cythonize(
    Extension(
        "pylon2d.Physics.PhysicsSys",  # Python module path
        [os.path.join(package_dir, "Physics", "PhysicsSys.pyx")],  # actual file path
    ),
    language_level="3",
)

setup(
    name="pylon2d",
    packages=["pylon2d", "pylon2d.Physics"],  # explicitly list packages
    ext_modules=ext_modules,
)
