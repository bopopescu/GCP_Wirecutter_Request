from google.appengine.api import urlfetch
# import requests

# response = requests.get("https://api.thedogapi.com/v1/breeds"); 


try:
   form_data = urllib.urlencode(UrlPostHandler.form_fields)
   headers = {
        'X-Api-Key': 'xmQsE6BowZel9xM5hDyFr4PI',
    },
     auth : {
       'username': 'nytimes',
       'password': 'EWp9rsWSB4pL28'
   }
   result = urlfetch.fetch(
       url='https://phoenix.submarineleisureclub.com/api/1.0/sources/1322',
       payload=form_data,
       method=urlfetch.GET,
       headers=headers)
   self.response.write(result.content)
except urlfetch.Error:
   logging.exception('Caught exception fetching url')







# url = 'https://api.thedogapi.com/v1/breeds'
# try:
#     result = urlfetch.fetch(url)
#     if result.status_code == 200:
#         self.response.write(result.content)
#     else:
#         self.response.status_code = result.status_code
# except urlfetch.Error:
#     logging.exception('Caught exception fetching url')