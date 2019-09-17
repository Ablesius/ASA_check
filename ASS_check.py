#! /usr/bin/env python3
"""TODO: doc string"""
from sys import argv
import pyalpm


def setup():
    """TODO DOCSTRING"""
    handle = pyalpm.Handle(r"/", r"/var/lib/pacman")
    localdb = handle.get_localdb()
    return handle, localdb


def filter_packages(localdb, packages: list):
    """Given a list of packages, return only those installed on the system"""
    filtered_packages = []
    for package in packages:
        filtered_package = localdb.get_pkg(package)
        if filtered_package:
            filtered_packages.append(filtered_package)
    return filtered_packages


def print_results(packages: list):
    """Print the packages installed in the system with their versions"""
    print("The following packages are installed with their corresponding version:")
    for package in packages:
        print(package.name, package.version)


def main():
    packages = argv[1:]
    handle, localdb = setup()
    filtered_packages = filter_packages(localdb, packages)
    print_results(filtered_packages)


if __name__ == '__main__':
    main()
