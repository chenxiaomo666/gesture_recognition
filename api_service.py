import base64
import requests


def send():
    token = get_token()
    img = hand_img()
    request_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture?access_token='+token

    params = {"image": img}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    print(response.json())


def get_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=atZp8l994lMkGTroIKCQf2FV&client_secret=6HoLmd6NOHsukBU7ZbElt7YbeqOYk92Q"
    r = requests.get(url)
    return r.json()['access_token']


def hand_img():
    f = open('demo.jpg', 'rb')
    img = base64.b64encode(f.read())
    return img


if __name__ == "__main__":
    send()
