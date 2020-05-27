import os
import base64
import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print('\n')
print('BLACKBOARD COURSE DOWNLOADER:')
print('\n')
school_url = input("Enter your school's Blackboard site in this format: blackboard.MYSCHOOL.edu \n")
school_url = f'https://{school_url}'
print('\n')
s_session_id = input("Enter the s_session_id associated with your Blackboard account: \n")
print('\n')
course_id = input("Enter the ID for the course whose directory you want to download: \n")
print('\n')
content_id = input("Enter the content ID for the folder or section to download: \n")
print('\n')

headers = { 
    'Cookie': f's_session_id={s_session_id}',
}

#633BC3EF28AD0A80CA8482DE2F32A607


def downloadFile(input_id, input_path):
    r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{input_id}/attachments', headers=headers, verify=False)
    attachmentsJSON = r.json()
    if attachmentsJSON['results'] == []:
        pass
    else:
        for item in attachmentsJSON['results']:
            attachment_id = item['id']
            title = item['fileName']
        r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{input_id}/attachments/{attachment_id}/download', headers=headers, allow_redirects=True, verify=False)
        url = r.url.rsplit("?", 1)[0] + " "
        extension = url[-4:]
        with open(f'{input_path}{title}.{extension}', 'wb') as file:
            file.write(r.content)

def iterateDirectory(input_json, input_path):
    root_path = input_path
    for item in input_json['results']:
        if item['contentHandler']['id'] == 'resource/x-bb-document':
            layer_id = item['id']
            downloadFile(layer_id, root_path)
        if item['contentHandler']['id'] == 'resource/x-bb-folder':
            layer_id = item['id']
            title = item['title']
            layer_path = f'{root_path}{title}/'
            os.mkdir(layer_path)
            r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{layer_id}/children', headers=headers, verify=False)
            layer_JSON = r.json()
            iterateDirectory(layer_JSON, layer_path)
           
r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{content_id}/children', headers=headers, verify=False)
root_JSON = r.json()
root_path = ''

print("Working...")
for item in root_JSON['results']:
    if item['contentHandler']['id'] == 'resource/x-bb-document':
        layer_id = item['id']
        downloadFile(layer_id, root_path)
    if item['contentHandler']['id'] == 'resource/x-bb-folder':
        layer_id = item['id']
        title = item['title']
        layer_path = f'{root_path}{title}/'
        os.mkdir(layer_path) 
        r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{layer_id}/children', headers=headers, verify=False)
        layer_JSON = r.json()
        iterateDirectory(layer_JSON, layer_path)


print('\n')
print('Done!')



    


        
                    
        
    

        
        
        

 
    








                                                                                                                                                                          

