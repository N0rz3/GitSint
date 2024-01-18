#!/usr/bin/env python3

__author__ = "N0rz3"

if __name__ == "__main__":
    import os; os.system("title GitSint")
    import sys; sys.dont_write_bytecode = True
    from lib.banner import banner; print(banner)
    from main import check_python_version; check_python_version()
