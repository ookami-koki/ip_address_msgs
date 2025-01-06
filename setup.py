from setuptools import find_packages, setup
package_name = 'ip_address_msgs'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='koki',
    maintainer_email='koki4302000@gmail.com',
    description='robosys 2024 practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
