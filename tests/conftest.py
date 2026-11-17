"""
conftest.py  [Shared test setup]
================================
Stage 3   Shared fixtures now disable tracking and select a local model before API imports
          New external services must not make the existing synthetic tests depend on accounts or a network
Purpose   Settings and fixtures every test file can use (pytest loads this file automatically)
Typical   switch tracking off and force the local model BEFORE src.api is imported
Why       Tests must be hermetic: no internet, no accounts, no secrets, same result everywhere
"""
