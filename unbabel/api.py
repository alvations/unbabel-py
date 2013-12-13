'''
Created on Dec 13, 2013

@author: joaograca
'''



import requests
import json

UNBABEL_API_URL="http://127.0.0.1:8000/tapi/v2/"
UNBABEL_USERNAME="gracaninja"
UNBABEL_APIKEY="5a6406e31f77ef779c4024b1579f0f6103944c5e"

class UnbabelApi(object):
    
    def __init__(self, *args, **kwargs):
        object.__init__(self, *args, **kwargs)

    def post_translations(self,text,target_language,
                          source_language=None,
                          type=None,
                          tone=None,
                          visibility=None,
                          public_url=None
                          ):
        
        headers={'Authorization': 'ApiKey %s:%s'%(UNBABEL_USERNAME,UNBABEL_APIKEY),'content-type': 'application/json'}
        data = {
                "text":text,
                "target_language":target_language
                }
        result = requests.post("%stranslation/"%UNBABEL_API_URL,headers=headers,data=json.dumps(data))
        if result.status_code == 201:
            return json.loads(result.content)
        else:
            return result

    def get_translations(self):
        '''
            Returns the translations requested by the user
        '''
        headers={'Authorization': 'ApiKey %s:%s'%(UNBABEL_USERNAME,UNBABEL_APIKEY),'content-type': 'application/json'}
        result = requests.get("%stranslation/"%UNBABEL_API_URL,headers=headers)
        return json.loads(result.content)
    
    
    def get_translation(self,id):
        '''
            Returns a translation with the given id
        '''
        headers={'Authorization': 'ApiKey %s:%s'%(UNBABEL_USERNAME,UNBABEL_APIKEY),'content-type': 'application/json'}
        result = requests.get("%stranslation/%s/"%(UNBABEL_API_URL,id),headers=headers)
        return json.loads(result.content)
    

    def get_language_pairs(self):
        '''
            Returns the language pairs available on unbabel
        '''
        headers={'Authorization': 'ApiKey %s:%s'%(UNBABEL_USERNAME,UNBABEL_APIKEY),'content-type': 'application/json'}
        result = requests.get("%slanguage_pair/"%UNBABEL_API_URL,headers=headers)
        return json.loads(result.content)
    
    def get_tones(self):
        '''
            Returns the tones available on unbabel
        '''
        headers={'Authorization': 'ApiKey %s:%s'%(UNBABEL_USERNAME,UNBABEL_APIKEY),'content-type': 'application/json'}
        result = requests.get("%stone/"%UNBABEL_API_URL,headers=headers)
        return json.loads(result.content)
    
    
