```
temperature-query-api
├─ .circleci
│  └─ config.yml
├─ .github
│  └─ PULL_REQUEST_TEMPLATE.md
├─ .gitignore
├─ .pre-commit-config.yaml
├─ .talismanrc
├─ LICENSE
├─ Makefile
├─ README.md
├─ docker
│  ├─ dev
│  │  ├─ Dockerfile
│  │  ├─ docker-compose.yml
│  │  └─ nginx
│  └─ test
│     ├─ Dockerfile
│     └─ docker-compose.yml
├─ env.example
├─ manage.py
├─ pytest.ini
├─ requirements.txt
├─ scripts
│  ├─ dev.sh
│  ├─ test.sh
│  └─ utils.sh
└─ src
   ├─ __init__.py
   ├─ api
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ migrations
   │  │  └─ __init__.py
   │  ├─ models.py
   │  ├─ urls.py
   │  ├─ utils
   │  │  ├─ __init__.py
   │  │  ├─ compute_temperature.py
   │  │  ├─ errors.py
   │  │  ├─ exception.py
   │  │  ├─ serializers.py
   │  │  └─ weatherapi_response.py
   │  └─ views.py
   ├─ app
   │  ├─ __init__.py
   │  ├─ asgi.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  └─ wsgi.py
   └─ tests
      ├─ __init__.py
      ├─ base_test.py
      ├─ test_api.py
      └─ test_calculations.py

```
