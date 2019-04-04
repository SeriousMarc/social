Test assignment for https://www.starnavi.io/vacancy/junior-python-developer
Time spent for the current task is 1 day.


### run tests

python manage.py test users
python manage.py test posts


### curl/http testing

## user login
http post http://0.0.0.0:8000/api/token/ username=<username> password=<password>

## user signup
# signup email hunter test

curl -H "content-type: application/json" \
-d '{"username":"<username>", "email":"test@test.test", "password":"<password>"}' \
-X post http://0.0.0.0:8000/api/users/signup/

# signup default and clearbit test

curl -H "content-type: application/json" \
-d '{"username":"<username>", "email":"alex@clearbit.com", "password":"<password>"}' \
-X post http://0.0.0.0:8000/api/users/signup/

## post creation
curl -H "Authorization: Bearer <token>" \
 -H "content-type: application/json" \
 -d '{"title":"<title>", "slug":"<slug>", "body":"<text>", "status":"0"}' \
 -X post http://0.0.0.0:8000/api/posts/create/

## post like
http http://0.0.0.0:8000/api/posts/<pk>/like/ "Authorization: Bearer <token>"

## post unlike
http http://0.0.0.0:8000/api/posts/<pk>/dislike/ "Authorization: Bearer <token>"