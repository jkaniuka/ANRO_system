from setuptools import setup
from glob import glob
import os
from Cython.Build import cythonize

package_name = 'dobot_control_panel'

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
        ('share/' + package_name + '/resource', ['resource/DobotControlPanel_layout.ui']),
        ('share/' + package_name, ['plugin.xml']),
        ('share/' + package_name + '/resource/images', glob('resource/images/*.png')),
        ('share/' + package_name + '/resource/images', glob('resource/images/*.svg'))
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
            'dobot_control_panel = dobot_control_panel.main:main',
        ],
    },
)

