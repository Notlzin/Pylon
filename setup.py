# oh yeah this was made by GPT-5mini, so uhh excuse me #
from setuptools import setup, Extension # type: ignore
from Cython.Build import cythonize
import os

here = os.path.dirname(__file__)  # outer root folder #
package_dir = os.path.join(here, "pylon2d")  # inner package folder #

ext_modules = cythonize(
    Extension(
        "pylon2d.Physics.PhysicsSys",  # python module path #
        [os.path.join(package_dir, "Physics", "PhysicsSys.pyx")],  # actual file path #
    ),
    language_level="3",
)

setup(
    name="pylon2d",
    packages=["pylon2d", "pylon2d.Physics"],  # explicitly list packages #
    ext_modules=ext_modules,
)
