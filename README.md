# lab-working-with-local-workflows-and-shared-libs
A clean simple project with 2 shared libraries, an app, cd-ci, and local testing.


## Troubleshooting

### Libraries need unique ids for their main tests.

Clear all the `__pycache__` directories in the project.
```powershell
    gci __pycache__ -R -OutVariable "BaseName" | \
        ForEach-Object { rm -Path $_.FullName -Force -Recurse -ErrorAction SilentlyContinue  }
```