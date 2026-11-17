# Dockerfile  [Serving container recipe]
# -------------------------------------------------------------------
# Purpose   Package the API (not training) into one image that runs the same everywhere
# Uses      conda-lock.yml, config.yaml, src/, models/model.joblib (promoted model, baked in at release)
# Runs      uvicorn src.api:app on the port the host provides
# Built by  you locally, ci.yml (must build), deploy.yml publish-image on each release
#
# Typical layers
#   builder stage: pinned base, install the locked environment, keep only what the API imports
#   -> runtime stage: slim base, copy the environment, code and model
#   -> build args MODEL_VERSION and GIT_COMMIT reported by /health
#   -> non-root user -> health check (/health) -> start command
