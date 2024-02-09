To set up the project, follow these steps:

```bash
git clone https://github.com/HimanshuGarg47/matters.git
cd matters
python -m venv .env
.env/Scripts/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
