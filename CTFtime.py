import requests
from hashlib import md5

# constant variables
savefile = "CTFtime_hash.dat"
root = ''        # for automation purposes
url = 'https://ctftime.org/team/196656'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
tmp = ""

# requests sent
r = requests.get(url, headers=headers)

# make sure the request works first
if r.status_code == 200:
    # filter need lines
    for line in r.text.split('\n'):
        if "Country" in line:
            tmp += line + '\n'
    # generate new hash
    newhash = md5(tmp.encode('utf-8')).hexdigest()
    try:
        open(root + savefile, "r")
    except FileNotFoundError:
        open(root + savefile, "x")
    # check against old hash
    with open(root + savefile, 'r')as f:
        if f.readline() != newhash:
            print("[%] CTFtime Rank: Ng00m4lDhuhur rank changed\thttps://ctftime.org/team/196656")
            open(root + "CTFtime_hash.dat", "w").write(newhash)
    f.close()
else:
    print("[X] Check Failed")
