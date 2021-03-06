from setuptools import setup, find_packages

setup(name='gym_urbandriving',
      version='0.0.3',
      install_requires=["gym<=0.9.5",
                        "image",
                        "scipy",
                        "shapely",
                        "numpy",
                        "pygame",
                        "scikit-image",
                        "opencv-python",
                        "codecov"],
      include_package_data=True,
      packages = find_packages()
      
)
