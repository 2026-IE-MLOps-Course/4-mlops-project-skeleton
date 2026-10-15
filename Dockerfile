# Dockerfile  [Serving container recipe]
# -------------------------------------------------------------------
# Purpose   Package the API (not training) into one image that runs the same everywhere
# Uses      conda-lock.yml (exact environment), config.yaml, src/, optional models/
# Runs      uvicorn src.api:app on the port the host provides
# Built by  you locally, ci.yml (must build), and the cloud host on each release
#
# Typical layers
#   pinned base image -> working folder -> install locked environment
#   -> copy code (filtered by .dockerignore) -> expose port -> health check (/health) -> start command
