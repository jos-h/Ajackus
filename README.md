# Ajackus

Steps to run the application
1. Clone the repo on you machine
2. Check if Python 3.x is installed if not then need to install Python >=3.6
3. Install Django >=3 and DjangoRestFramework (DRF) == 3.11.0
4. Check if pip is installed on your machine.
5. Pip is required to run the requirements.txt file to install the dependencies required.
6. pip install -r requirements.txt
7. Use of reportlab package to create pdf file and store in the media folder inside the application
8. Seed_data.py file present inside the app/management/command folder to create the seed data for admin users using following command
          python manage.py seed_data.py
9. Run makemigrations command first and then migrate command so the necessary DB changes would get affected
      python manage.py makemigrations
      python manage.py migrate
10. I have teste the api using postman manually
11. Run the app on local server python manage.py runserver


Features:-
1. To use AWS bucket to upload the pdf files and store the location in the DB.
