# Hello Action

Sample and testing project for github actions and deployment to Azure Function using pipenv, flake8 and pytest.

## What it does

Runs two actions in 2 Github workflows for a python project setup with pipenv.
Also, Github caching is used to speed up the workflow by loading re-used dependencies from cache instead of redownloading them each build.
Note: Although mypy (type checking) is configured, it is not setup as a workflow step.

### Test

- Runs on every push to any branch in the repo.
- This also includes pull requests being merged as they always result in a push as well.
- Multiple steps are configured here, such as running `pytest` as well as a linter with `flake8`.
- The build step therefore includes the --dev dependencies from your Pipfile as well`

### Deploy

- Triggers when the Test workflow passed on the `main` branch,
- Builds the project with pipenv,
- Deploys to an Azure Function App.

## What's needed

- Download the Publish profile from the Azure Function app,

- Store it in the Github Repo as a secret, with a name "AZURE_CREDENTIALS" (or whatever you define in the last step of `deploy.yml`).
