creating conda environment
"""
conda create -p env python==3.7 -y

"""
activate conda environment
"""
conda activate env/

or

conda activate env

"""

"""
pip install -r requirements.txt

"""
To Add files to git
"""
git add .

or 

git add <file_name>

"""
> note : to ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
"""
git status
"""
to check all version maintained by git
"""
git log
"""
To create version /commit all changes by git
"""
git commit -m "message"
"""
To send version /changes to github
"""
git push origin main
"""
To check remote url
"""
git remote -v
"""

To setup CI/CD pipeline in heroku we need 3 information

1.HEROKU_EMAIL = 
2.HEROKU_API_KEY = 
3.HEROKU_APP_NAME = 

BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .

Note: Image name for docker must be lowercase

To list docker image

docker images
Run docker image

docker run -p 5000:5000 -e PORT=5000 image id
To check running container in docker

docker ps

To stop docker conatiner

docker stop <container_id>

"""
python setup.py install

"""