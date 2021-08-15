# Deploy Immutables

This IaC component permit single-thread (multi-thread soon) deployment of immutable resources.

## Setup Development Environment

- Clone this repo: `git clone git@github.com:SindriaInc/deploy-immutables.git`
- Move into it: `cd deploy-immutables`
- Build local image: `bash build.sh sindriainc/deploy-immutables local`
- Setup env: `cp .env.local .env`
- Setup docker compose: `cp docker-compose.local.yml docker-compose.yml`
- Start environment: `docker-compose up -d`