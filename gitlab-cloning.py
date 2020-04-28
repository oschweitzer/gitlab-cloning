import gitlab
import os
import git

gitlab_host = os.getenv('GITLAB_HOST', "XXXXXXXX")
gitlab_token = os.getenv('GITLAB_TOKEN', "XXXXXXXX")
gitlab_username = os.getenv('GITLAB_USERNAME', "XXXXXXXX")
gitlab_password = os.getenv('GITLAB_PASSWORD', "XXXXXXXX")
group_id = os.getenv('GROUP_ID', 1)
repositories_root_dir = os.getenv('REPOSITORIES_ROOT_DIR', '.')
cloning_mode = os.getenv('CLONING_MODE', 'http').lower()

gl = gitlab.Gitlab(gitlab_host, private_token=gitlab_token, ssl_verify=False, api_version=4)
group = gl.groups.get(group_id)
projects = group.projects.list(as_list=False)
for project in projects:
    print(project.name)
    if not os.path.exists(os.path.join(repositories_root_dir, project.name.lower())):
        if cloning_mode == 'ssh':
            # SSH version
            git.Git(repositories_root_dir).clone(project.ssh_url_to_repo)
        elif cloning_mode == 'http':
            # HTTPS version
            git.Git(repositories_root_dir).clone(f'https://{gitlab_username}:{gitlab_password}@{project.http_url_to_repo.split("https://")[1]}')
        else:
            raise Exception('Error: no valid cloning mode provided')