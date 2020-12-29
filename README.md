# Setup

Install all the required packages: `pip install -r requirements.txt` and
add your Discord Webhook URLs in core/hooks.py.

 1. `python manage.py makemigrations`
 2. `python manage.py migrate`
 3. `python manage.py createsuperuser`
 4. Go to the [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and create an object in the `Person` model. Here, you can associate the person to the admin(you) or create another user in the `User` default model to associate it to. Make sure you tick the `is_admin` to make the person capable of making students from the website.
 5. Go to  [http://127.0.0.1:8000/admin_dashboard/](http://127.0.0.1:8000/admin_dashboard/) and you're pretty much done. Create teachers and students from there and you can log in with their account!

***Contributions are welcomed !!!***

If you don't know `git` : https://git-scm.com/docs/gittutorial 
