deactivate

if(-not (test-path .\Scripts))
{
    python -m venv .
}
.\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
