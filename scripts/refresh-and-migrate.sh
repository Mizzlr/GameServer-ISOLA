cd backend

find . -name "00*.pyc" -exec rm -f {} \;
find . -name "00*.py" -exec rm -f {} \;

rm db.sqlite3

python3 manage.py makemigrations
python3 manage.py migrate