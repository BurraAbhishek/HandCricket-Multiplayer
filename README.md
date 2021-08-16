# HandCricket-Multiplayer
The Multiplayer version of Python-Hand-Cricket, using the Django framework

This website is written in [Python 3](https://www.python.org/) using the [Django](https://www.djangoproject.com/) framework. HTML is used for templating. It uses [MongoDB](https://mongodb.org/) to store  games as JSON documents. MongoDB connections are handled using [PyMongo](https://github.com/mongodb/mongo-python-driver) and [Djongo](https://github.com/nesdis/djongo). The CSS stylesheets are written into HTML &lt;style&gt; tags. Sessions and cached data are handled using [redis](https://redis.io). The Django admin site is not used here in favour of moderator accounts.

## Installation

If you have only Python 3.x installed:
```
python manage.py migrate
python manage.py runserver
```

If you have both Python 2.x and Python 3.x installed:
```
python3 manage.py migrate
python3 manage.py runserver
```

Use `localhost:8000` to open this website.

## License

HandCricket-Multiplayer is licensed under the GNU Affero General Public License 3 or any later version at your choice.
