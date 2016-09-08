from __future__ import print_function
from __future__ import absolute_import
from instagram import client

config = {
    'id': 'instagram',
    'name': 'Instagram',
    'install': 'pip install python-instagram',
    'module': 'flask_social.providers.instagram',
    'base_url': '',
    'authorize_url': client.InstagramAPI.authorize_url,
    'access_token_url': client.InstagramAPI.access_token_url,
    'request_token_url': None,
    'access_token_method': 'POST',
    'request_token_params': {
        'scope': ['basic', 'public_content']
    },
}


def get_api(connection, **kwargs):
    print(__name__, 'get_api', connection, kwargs)
    return client.InstagramAPI(
        client_id=kwargs.get('consumer_key'),
        client_secret=kwargs.get('consumer_secret'),
        access_token=connection.access_token,
    )


def get_provider_user_id(response, **kwargs):
    if response:
        profile = response['user']
        return profile['id']

    return None


def get_connection_values(response, **kwargs):
    if not response:
        return None

    profile = response['user']
    return dict(
        provider_id=config['id'],
        provider_user_id=profile['id'],
        access_token=response['access_token'],
        secret=None,
        display_name=profile['username'],
        full_name=profile['full_name'],
        profile_url='https://www.instagram.com/%s/' % profile['username'],
        image_url=profile['profile_picture'],
    )


def get_token_pair_from_response(response):
    return dict(
        access_token=response.get('access_token', None),
        secret=None,
    )
