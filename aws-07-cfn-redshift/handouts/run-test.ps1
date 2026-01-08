###
### PowerShell Script to run local unit tests with pytest
###

### You can run ./install-tests.ps1 before this file

# Directory may need to be changed depending on where the .venv has been installed
.venv\Scripts\activate.ps1

Write-Output "Running pytest..."
python3 -m pytest -v -s
