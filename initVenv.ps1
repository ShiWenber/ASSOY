deactivate


if(-not (test-path .\Scripts))
{
    python -m venv .
}

.\Scripts\activate
python -m pip install --upgrade pip

pip freeze > requirements_temp.txt
pip uninstall -r requirements_temp.txt
remove-item requirements_temp.txt
pip install -r requirements.txt