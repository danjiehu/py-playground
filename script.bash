# OVERVIEW: start a python3 virtual environment, install django and djangorestframework

mkdir expense_calculator
cd expense_calculator

#  1. create a virtual environment
# A virtual environment is an isolated Python environment that allows you to manage dependencies and packages separately for different projects. 
# The virtual environment is just like any other environment, so you can use pip to install Django and djangorestframework.
python3 -m venv venv

#  2. activate the virtual environment
# This command activates the virtual environment. When activated, it modifies your shell's environment variables to use the Python interpreter and packages installed within the virtual environment instead of the system-wide Python installation. The prompt will change to indicate that you are now working within the virtual environment.
source venv/bin/activate

#  3. install django and djangorestframework
pip install django djangorestframework

#  4. create a django project
# This command below creates a Django project named expense_calculator in the current directory.
django-admin startproject expense_calculator .
# Create a Django app named "expenses" within the project
django-admin startapp expenses
# Run the Django development server
python manage.py runserver