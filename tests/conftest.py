"""
conftest.py  [Shared test setup]
================================
Purpose   Settings and fixtures every test file can use (pytest loads this file automatically)
Typical   switch tracking off and force the local model BEFORE src.api is imported
Why       Tests must be hermetic: no internet, no accounts, no secrets, same result everywhere
"""
