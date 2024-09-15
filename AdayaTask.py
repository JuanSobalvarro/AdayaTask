import argparse
import os
import sys
import unittest
import src.run as r


def run_tests():
    """
    Function to run all tests.
    """
    tests = unittest.TestLoader().discover('.', pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)


def run_app(debug=False):
    """
    Function to run the app. If debug=True, run in debug mode.
    """
    if debug:
        print("Running in debug mode...")
    r.run(debug)


def main():
    parser = argparse.ArgumentParser(description='AdayaTask Command Line Options')
    parser.add_argument('--test', action='store_true', help='Run all tests')
    parser.add_argument('--debug', action='store_true', help='Run app in debug mode')

    args = parser.parse_args()

    if args.test:
        run_tests()
    elif args.debug:
        run_app(debug=True)
    else:
        run_app()


if __name__ == '__main__':
    main()
