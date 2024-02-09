To set up the project, follow these steps:

```bash
git clone <repository_url>
cd matters
python -m venv .env
.env/Scripts/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
