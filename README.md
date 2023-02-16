SQL Injection Demo
==========

Execute Server
----------
```
python main.py
```

Test Server
----------
Tests are executed on Windows
```
curl -d "username=felix&password=pwfelix" -X POST http://localhost:5000/login_form_vulnerable

```
