import urllib

import requests



class PivotalClient(object):

    tracker_token = None
    api_uri = None
    projects = None

    PROJECT_ENTITIES = ('stories',)

    def __init__(self, **kwargs):

        self.tracker_token = kwargs.get('tracker_token')
        if not self.tracker_token:
            raise ValueError('tracker_token not set')

        self.api_uri = kwargs.get('api_uri')
        if not self.api_uri:
            raise ValueError('api_uri not set')
        if self.api_uri[-1] != '/':
            self.api_uri += '/'

        self.projects = kwargs.get('projects')
        if not self.projects:
            self._init_projects()
        
    def _serialize_uri_params(self, **params):
        return '&'.join(
            [
                "{}={}".format(
                    k,
                    urllib.parse.quote_plus(v)
                ) for k, v in params.items()
            ]
        )

    def _prepare_headers(self):
        return {
            'X-TrackerToken': self.tracker_token
        }

    def _init_projects(self):
        self.projects = []
        r = requests.get(self.api_uri+'/projects', headers=self._prepare_headers())
        for i in r.json():
            self.projects.append(i['id'])

    def _create_path(self, project, entity):
        if entity in self.PROJECT_ENTITIES:
            return 'projects/{}/{}'.format(project, entity)
        else:
            return entity

    def get(self, entity, **params):
        if entity[0] == '/':
            entity = entity[1:]
        items = []
        for project in self.projects:
            path = self._create_path(project, entity)
            uri = '{}{}?{}'.format(
                self.api_uri,
                path,
                self._serialize_uri_params(**params)
            )
            headers = self._prepare_headers()
            r = requests.get(uri, headers=headers)
            r.raise_for_status()
            items += [item for item in r.json() if item not in items]
        return items
    
    def me(self):
        uri = '{}{}'.format(
            self.api_uri,
            self._create_path(self.projects[0], 'me'),
        )
        r = requests.get(uri, headers=self._prepare_headers())
        r.raise_for_status()
        return r.json()
    