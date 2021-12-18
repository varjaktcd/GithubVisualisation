# GithubVisualisation

In powershell, run these on the directory of the code
```
CODE_DIRECTORY\venv\Scripts\python.exe -m pip install --upgrade pip
```

```
docker compose build
```

```
docker compose up
```
## Automatic Run
Run the shell script ```run.sh``` to have the program automatically execute.

This can be done with the command ```./run.h```.


## Manual Run
Run ```main.py``` to create the database.

Run ```process.py``` to acess the database and process its data.

Run ```cleardb.py``` if you wish to clear the database to try the program again.
  
I've included shell scripts if you wish to use those. They can be run using:

```./shellscriptname.sh```
