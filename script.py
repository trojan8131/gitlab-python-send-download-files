
import gitlab
from base64 import b64encode
from pprint import pprint
# authenticate with GitLab
gl = gitlab.Gitlab('https://tenant.gitlab.com/', private_token='glpat-Daj9Z82G3G7RzZyWFWAS')
project = gl.projects.get('project')

# Send new file
remote_file_path = 'router_config_form.xlsm'

with open(remote_file_path, 'rb') as f:
    bin_content = f.read()
b64_content = b64encode(bin_content).decode('utf-8')

f = project.files.create({'file_path': remote_file_path,
                          'branch': 'main',
                          'content': b64_content,
                          'author_name': 'Automation',
                          'encoding': 'base64',  # important!
                          'commit_message': 'Create file'})


# Download that file 

file_content = project.files.get(file_path=remote_file_path, ref='main').decode()

# Save localy
local_file_path = 'router_config_form_git.xlsm'
with open(local_file_path, 'wb') as file:
    file.write(file_content)

