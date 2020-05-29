import os
import base64
import json
import requests
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def downloadLink(input_id, input_path):
    r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{input_id}/attachments', headers=headers, verify=False)
    attachments_json = r.json()
    if attachments_json['results'] == []:
        pass
    else:
        for item in attachments_json['results']:
            attachment_id = item['id']
            title = item['fileName']
        r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{input_id}/attachments/{attachment_id}/download', headers=headers, allow_redirects=True, verify=False)
        with open(f'{input_path}{title}', 'wb') as file:
            file.write(r.content)
        print(title)
            
def downloadFile(input_id, input_path):
    r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{input_id}/attachments', headers=headers, verify=False)
    attachments_json = r.json()
    if attachments_json['results'] == []:
        pass
    else:
        for item in attachments_json['results']:
            attachment_id = item['id']
            title = item['fileName']
            r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{input_id}/attachments/{attachment_id}/download', headers=headers, allow_redirects=True, verify=False)
            url = r.url.rsplit("?", 1)[0] + " "
            extension = url[-4:]
            with open(f'{input_path}{title}.{extension}', 'wb') as file:
                file.write(r.content)
            print(f'{title}.{extension}')

    
def iterateDirectory(input_json, input_path):
    root_path = input_path
    for item in input_json['results']:
        if item['availability']['allowGuests'] == False:
            continue
        if item['contentHandler']['id'] == 'resource/x-bb-document':
            layer_id = item['id']
            downloadFile(layer_id, root_path)
        if item['contentHandler']['id'] == 'resource/x-bb-externallink':
            url = item['contentHandler']['url']
            title = item['id']
            with open(f'{root_path}{title}.txt', 'wb') as file:
                file.write(url.encode())
        if item['contentHandler']['id'] == 'resource/x-bb-file':
            layer_id = item['id']
            downloadLink(layer_id, root_path)
        if item['contentHandler']['id'] == 'resource/x-bb-courselink':
            bug = item['id']
            layer_id = item['contentHandler']['targetId']
            r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{layer_id}', headers=headers, verify=False)
            verify_json = r.json()
            if verify_json['contentHandler']['id'] == 'resource/x-bb-file':
                downloadLink(layer_id, root_path)
            else:
                continue
        if item['contentHandler']['id'] == 'resource/x-bb-folder':
            layer_id = item['id']
            title = item['title']
            if '/' in title:
                title = title.replace('/', '-')
            if ':' in title:
                title = title.replace(':', '')
            if '"' in title:
                title = title.replace('"', '')
            if '"' in title:
                title = title.replace('\\', '-')
            if '*' in title:
                title = title.replace('*', '')
            if '?' in title:
                title = title.replace('?', '')
            layer_path = f'{root_path}{title}/'
            os.mkdir(layer_path)
            r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{layer_id}/children', headers=headers, verify=False)
            layer_JSON = r.json()
            iterateDirectory(layer_JSON, layer_path)

print('\n')
time.sleep(1)
print('BLACKBOARD COURSE DOWNLOADER: https://github.com/katurian/getBlackboardDirectory')
time.sleep(1)
print('Buy me a coffee: https://ko-fi.com/katski')
time.sleep(1)
print('Hire me: https://katski.org/')
print('-----------------------------------------------')
time.sleep(.5)
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
           
r = requests.get(f'{school_url}/learn/api/public/v1/courses/{course_id}/contents/{content_id}/children', headers=headers, verify=False)
root_json = r.json()
root_path = ''

print("Working...")
print('\n')

iterateDirectory(root_json, root_path)

print('\n')
print('Done!')
