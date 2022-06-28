from cmath import e
import json
from flask import request, abort, jsonify
from functools import wraps
from jose import jwt
from urllib.request import urlopen
from settings import AUTH0_DOMAIN_SETTING, ALGORITHMS_SETTING, \
    API_AUDIENCE_SETTING

# https://fsnd-coffeeshop-udacity.us.auth0.com/authorize?audience=Capstone&&scope=SCOPE&response_type=token&client_id=4xI59Nc5cJMw20YZuMqwOOAZy6GTqeSp&redirect_uri=http://127.0.0.1:8080/

# , https://capstone-project-2022-udacity.herokuapp.com/
# , https://capstone-project-2022-udacity.herokuapp.com/login_result

# // https://fsnd-coffeeshop-udacity.us.auth0.com/authorize?audience=Capstone&scope=SCOPE&response_type=token&client_id=4xI59Nc5cJMw20YZuMqwOOAZy6GTqeSp&redirect_uri=https://capstone-project-2022-udacity.herokuapp.com/
# //DATABASE_URL = 'postgresql://tewlagpxaiibfj:f10386641326ff8c509ac88f310b53ca0f282c7ffad4cde37c6fac74d018f3f7@ec2-54-147-33-38.compute-1.amazonaws.com:5432/ds7ovkldr81jo'

AUTH0_DOMAIN = AUTH0_DOMAIN_SETTING
ALGORITHMS = ALGORITHMS_SETTING
API_AUDIENCE = API_AUDIENCE_SETTING


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():

    auth = request.headers.get('Authorization', None)

    if not auth:
        raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'Authorization header is expected.'
        }, 401)

    parts = auth.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must start with "Bearer".'
        }, 401)

    elif len(parts) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found.'
        }, 401)

    elif len(parts) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be bearer token.'
        }, 401)

    token = parts[1]
    return token


def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, \
                    check the audience and issuer.'

            }, 401)
        except Exception as e:
            print("EXCEPTION", e)
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
    }, 400)


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        abort(400)

    if permission not in payload['permissions']:
        abort(403)

    return True


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            jwt = get_token_auth_header()

            try:
                payload = verify_decode_jwt(jwt)
            except BaseException as e:
                print("Exception:", e)
                return(verify_decode_jwt(jwt))
                # abort(401)

            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
