from service import zoho_authentification
from utility import handler_process_utils
import json
import requests



def get_attachment_id(attachment_list):
    if "data" not in attachment_list:
        return ""
    data = attachment_list["data"]
    
    for i in range(100):
        file_name = data[i]["File_Name"]
        attachment_id = data[i]["id"]
        if file_name.endswith("_Firmado.pdf"):
            return attachment_id
        else:
            continue

def get_attachments(idld):

    url = 'https://www.zohoapis.com/crm/v2/Lineas_de_defensa/' + idld + '/Attachments'

    token = zoho_authentification.get_token()

    headers = {
        'Authorization': 'Zoho-oauthtoken ' + token
    }

    parameters = {
        # 'fields': 'id',
        'page': 1,
        'per_page': 20
    }

    response = requests.get(url=url, headers=headers, params=parameters)

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        return response.json()



def download_attachment(idld, attacment_id, ldname):

    url = 'https://www.zohoapis.com/crm/v2/Lineas_de_defensa/' + idld + '/Attachments/' + attacment_id

    token = zoho_authentification.get_token()
    
    headers = {
        'Authorization': 'Zoho-oauthtoken ' + token
    }

    response = requests.get(url=url, headers=headers)

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        if 'Content-Type' in response.headers:
            content_type = response.headers['Content-Type'].split(';')[0]

            if content_type == 'application/json':
                print(response.json())
            else:
                if 'Content-Disposition' in response.headers:
                    file_name = ''
                    content_disposition = response.headers['Content-Disposition']

                    if "'" in content_disposition:
                        start_index = content_disposition.rindex("'")
                        file_name = content_disposition[start_index + 1:]

                    elif '"' in content_disposition:
                        start_index = content_disposition.rindex('=')
                        file_name = content_disposition[start_index + 1:].replace('"', '')

                    filename = ldname.replace("-", "_") + ".pdf"
                    destination_file = filename

                    with open(destination_file, 'wb') as f:
                        for chunk in response:
                            f.write(chunk)
    return filename


def update_records(idld, radicado_nos):

    token = zoho_authentification.get_token()

    url = 'https://www.zohoapis.com/crm/v2/Lineas_de_defensa'

    headers = {
        'Authorization': 'Zoho-oauthtoken ' + token,
    }

    request_body = dict()
    record_list = list()
    record_object_1 = {
        'id': idld,
        'Estado': 'Radicado',
        'Radicado': radicado_nos,
        'Fecha_de_radicaci_n': handler_process_utils.datetime_utc_now_CRM()
    }

    record_list.append(record_object_1)

    request_body['data'] = record_list

    trigger = [
        'approval',
        'workflow',
        'blueprint'
    ]

    request_body['trigger'] = trigger

    response = requests.put(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        print(response.json())


def update_records(idld, radicado_nos):

    token = zoho_authentification.get_token()

    url = 'https://www.zohoapis.com/crm/v2/Lineas_de_defensa'

    headers = {
        'Authorization': 'Zoho-oauthtoken ' + token,
    }

    request_body = dict()
    record_list = list()
    record_object_1 = {
        'id': idld,
        'Estado': 'Radicado',
        'Radicado': radicado_nos,
        'Fecha_de_radicaci_n': handler_process_utils.datetime_utc_now_CRM()
    }

    record_list.append(record_object_1)

    request_body['data'] = record_list

    trigger = [
        'approval',
        'workflow',
        'blueprint'
    ]

    request_body['trigger'] = trigger

    response = requests.put(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        print(response.json())


def upload_an_attachment(idld, radicado_number):
    url = 'https://www.zohoapis.com/crm/v2/Lineas_de_defensa/' + idld + '/Attachments'

    token = zoho_authentification.get_token()

    headers = {
        'Authorization': 'Zoho-oauthtoken ' + token
    }

    request_body = {
        'file': open(
            "EVIDENCIA_"+ radicado_number + ".png",
            'rb')
    }

    response = requests.post(url=url, files=request_body, headers=headers)

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        return response.json()

