import requests



def get_token_crm():

    # variables to get token
    params = ""
    c_id = "1000.7ZGXHS25V6VAA83BD5WHXZWODU3XOT"
    c_secret = "60494d168d91d7186f745aed3a7f0bb2d09259da4a"
    g_type = 'refresh_token'
    url = 'https://accounts.zoho.com/oauth/v2/token'
    rt = '1000.53f46ddd007e145e571aed766aeef2b8.5295838fb6df30d143cbb601422d9b9c'
    
    parameters = dict(
        
        client_id=c_id,
        client_secret=c_secret,
        grant_type=g_type,
        refresh_token=rt         
    )

    if url is not None:

        # sending the request
        response = requests.post(url=url, params=parameters)
        response = response.json()

        # returning the result
        try:
            response = response['access_token']
            return response

        except KeyError:
            return None
    else:
        return None


def get_token():

    token = get_token_crm()
    return token