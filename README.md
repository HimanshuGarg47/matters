To set up the project, follow these steps:

```bash
git clone https://github.com/HimanshuGarg47/matters.git
cd matters
python -m venv .env
.env/Scripts/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


```
# go to URL for all API list and payload/json format    http://127.0.0.1:8001/api/schema/swagger-ui/
