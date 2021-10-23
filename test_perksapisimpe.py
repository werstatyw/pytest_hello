import requests
class TestAPIGetRequests:

   # def test_is_redirected(self):
       # response = requests.get(
       #     'https://test3.perksdev.com/api/v1/test',
      #       allow_redirects=True
     #   )
    #    assert response.url == 'https://test3.perksdev.com/api/v1/test'

   # def test_base_url_responds(self):
   #     response = requests.get(
   #         'https://test3.perksdev.com/api/v1/test',
  #           allow_redirects=False
 #       )
#        assert response.code == 200

    def test_ok_json_message(self):
        response = requests.get(
            'https://test3.perksdev.com/api/v1/test',
             allow_redirects=False
        )
        json = response.json()
        assert json['message'] == "OK"
        assert json['error'] == None
