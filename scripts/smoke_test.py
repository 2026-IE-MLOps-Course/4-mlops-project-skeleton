"""
smoke_test.py  [Is the deployed API alive and correct?]
=======================================================
Purpose   Check a RUNNING API (local, Docker or cloud): GET /health, then POST /predict
Input     API address + scripts/sample_request.json (+ optional expected commit and model version)
Output    Exit code 0 if healthy, 1 otherwise, so CI/CD can stop a bad release
Run by    you after "docker run", and deploy.yml twice per release:
          on the container before push, on the live URL after deploy

Why it matters
- Unit tests prove the code; this proves the deployed SERVICE answers correctly
- Standard library only, so it runs anywhere without installing packages
"""
