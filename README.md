# Gitlab Cloning

## Description

This repository contains a script written in Python that allows to clone all the projects from a Gitlab group using SSH or HTTP.

The following environment variables are available

| Name                  | Default value | Mandatory                               |
|-----------------------|---------------|-----------------------------------------|
| GITLAB_HOST           | "XXXXXXXX"    | yes                                     |
| GITLAB_TOKEN          | "XXXXXXXX"    | yes                                     |
| GITLAB_USERNAME       | "XXXXXXXX"    | only if CLONING_MODE is equal to "http" |
| GITLAB_PASSWORD       | "XXXXXXXX"    | only if CLONING_MODE is equal to "http" |
| GROUP_ID              | 1             | yes                                     |
| REPOSITORIES_ROOT_DIR | "."           | yes                                     |
| CLONING_MODE          | "http"        | yes                                     |

## Usage

I strongly advise to use virtual environment such as [Anaconda](https://www.anaconda.com/distribution/) to install and run this application.

### Example with Anaconda

1. `conda create --name gitlab-cloning python=3.7`
2. `conda activate gitlab-cloning`
3. `python pip install -r requirements.txt`
4. `GITLAB_HOST=https://myGitlab.com GITLAB_TOKEN=goodToken GROUP_ID=14 REPOSITORIES_ROOT_DIR=../myDir CLONING_MODE=http GITLAB_USERNAME=goodBoy GITLAB_PASSWORD=ultrastrongpassword python gitlab-cloning.py`