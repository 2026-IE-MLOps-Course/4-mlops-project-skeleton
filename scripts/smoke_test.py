"""
smoke_test.py  [Is the deployed API alive and correct?]
=======================================================
Stage 3   Local tests gain a check against a running service, first in a container and then online
          Confirm the released code and model answer requests before accepting the deployment
Purpose   Check a RUNNING API (local, Docker or cloud): GET /health, then POST /predict
Input     API address + scripts/sample_request.json (+ optional expected commit and model version)
Output    Exit code 0 if healthy, 1 otherwise, so CI/CD can stop a bad release
Run by    you after "docker run", and deploy.yml twice per release:
          on the container before push, on the live URL after deploy

Why it matters
- Unit tests prove the code; this proves the deployed SERVICE answers correctly
- Standard library only, so it runs anywhere without installing packages
"""
