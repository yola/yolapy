import os
import json


def _load_local_json(fn):
    with open(os.path.join(os.path.dirname(__file__), fn)) as f:
        return json.load(f)

subscriptions_for_userid = _load_local_json('subscriptions_for_userid.json')
