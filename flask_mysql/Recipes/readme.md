[python -m] pipenv install flask pymysql
[python -m] pipenv shell
            pipenv install flask-bcrypt

[server.py](server.py)
[user.py](user.py)
[mysqlconnection.py](mysqlconnection.py)

<input type="hidden" name="id" value="{{recipe.id}}">  

SELECT first_name FROM users JOIN recipes ON users.id = recipes.user_id
WHERE recipes.user_id= 7;

view
{% if recipe.user_id == session.user_id%}
edit
delete

{% endif %}