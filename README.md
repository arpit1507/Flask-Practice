# Flask-Practice
basic flask practice 
 
### steps to be performed: 
At the start of the project, we need to create a virtual environment and install Flask. 

```
conda create -n your-env-name python==3.7
activate your-env-name
```

### Install Required Packages
create a new file called `requirements.txt` and add the packages you want to install. 
eg:-
```
pip install Flask
```

### Storing the project
use git commands to access and edit the project files in the github repository.
```
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/your-username/your-project-name.git
git push -u origin master
```

### Creating the Flask app
create a new file called `app.py`. you can impliment the following code to create a basic flask app.
```
from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
```