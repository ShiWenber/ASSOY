deactivate

if(-not (test-path .\Scripts))
{
    python -m venv .
}
.\Scripts\activate
new-item .\input
new-item .\numTable
new-item .\strTable
new-item .\freeTable
python -m pip install --upgrade pip
pip install -r requirements.txt
