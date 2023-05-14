from flask import Flask
import flask, werkzeug.exceptions

INVITE = '' # must only be the code, omitting discord.gg
WEBHOOK = '' # must be a valid discord webhook URL (make sure this is not in a public channel)
SHEET_DB_KEY = '' # sheet db key only, no url

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.json.sort_keys = False

@app.errorhandler(werkzeug.exceptions.HTTPException)
def bad_request(e):
    response = flask.make_response({"status": f"{str(e)[:3]}", "url": f"https://http.cat/{str(e)[:3]}"})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/')
def index():
    return 'why does this app even have a frontend lolololol<br><a href="/api/push_count">push request</a>'

@app.route('/api/push_count')
def api_push_count():

    if INVITE == '' or SHEET_DB_KEY == '':
        response = flask.make_response({"status": f"500", "url": f"https://http.cat/200", 'missing info': 'please fill in the data on lines 4, 5, and 6, then redeploy.'})
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    from urllib.request import Request, urlopen
    from urllib import parse
    from datetime import datetime
    import json, requests

    now = datetime.now()
    string_time = now.strftime("%m/%d/%Y")
    invite_data = requests.get(f'https://discord.com/api/v9/invites/{INVITE}?with_counts=true').json()
    member_count = invite_data['approximate_member_count']
    server_name = invite_data['guild']['name']

    sheet_db_payload_data = parse.urlencode({
            'id':'INCREMENT', 
            'date':f'{string_time}', 
            'count':f'{member_count}'
        }).encode()
    urlopen(Request(f'https://sheetdb.io/api/v1/{SHEET_DB_KEY}', data=sheet_db_payload_data))

    if WEBHOOK == '':
        response = flask.make_response({"status": f"200", "url": f"https://http.cat/200"})
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    webhook_payload_data = json.dumps(
        {
            "content": None,
            "embeds": [
                {
                    "title": None,
                    "description": f"**updated server count for {server_name}**",
                    "color": None,
                    "fields": [{
                        "name": "count",
                        "value": f"{member_count}"
                    }, {
                        "name": "date",
                        "value": f"{string_time}"
                    }, {
                        "name": "invite code",
                        "value": f"{INVITE}"
                    }],
                    "timestamp": f"{datetime.now()}"
                }
            ],
            "attachments": []
        })
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Safari/537.11'}
    urlopen(Request(f'{WEBHOOK}', data=webhook_payload_data.encode(), headers=headers))

    response = flask.make_response({"status": f"200", "url": f"https://http.cat/200"})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response