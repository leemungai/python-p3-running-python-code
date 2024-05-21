#!/usr/bin/env python3

import os
import runpy
import io
import sys
import pytest

class TestAppPy:
    '''
    Tests for the app.py file.
    '''

    def test_app_py_exists(self):
        '''
        Checks if app.py exists in the lib directory.
        '''
        assert os.path.exists("lib/app.py"), "app.py does not exist in the lib directory"

    def test_app_py_runs(self):
        '''
        Checks if app.py is executable.
        '''
        runpy.run_path("lib/app.py")

    def test_prints_hello_world(self):
        '''
        Checks if app.py prints "Hello World! Pass this test, please."
        '''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            runpy.run_path("lib/app.py")
        finally:
            sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello World! Pass this test, please.\n", \
            f"Unexpected output: {captured_out.getvalue()}"

