from setuptools import setup
import os
from glob import glob
from Cython.Build import cythonize

package_name = 'dobot_bringup'

files = package_name + "/*.py"

setup(
    ext_modules=cythonize(files,compiler_directives={'language_level' : "3"},force=True,quiet=True),
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools', "wheel",  "Cython"],
    zip_safe=True,
    maintainer='jkaniuka',
    maintainer_email='kan.jan@wp.pl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'set_tool_null = dobot_bringup.set_tool_null:main',
            'connection_test = dobot_bringup.connection_test:main',
        ],
    },
)
