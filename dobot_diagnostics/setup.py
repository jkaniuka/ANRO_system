from setuptools import setup
import os
from glob import glob
from Cython.Build import cythonize

package_name = 'dobot_diagnostics'

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
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))),
    ],
    install_requires=['setuptools', "wheel",  "Cython"],
    zip_safe=True,
    maintainer='jan',
    maintainer_email='jan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'alarms_parser = dobot_diagnostics.alarms_parser:main',
            'alarm_clear = dobot_diagnostics.alarm_clear:main'
        ],
    },
)
