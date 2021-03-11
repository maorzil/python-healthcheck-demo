import json
import time

import requests

service_url = 'http://localhost:8080'
auth_token = '<ADD_TOKEN>'  # assumptions: user/bot has the relevant scopes
slack_channel_id = '<ADD_CHANNEL_ID>'
default_message = '<ADD_MESSAGE>'


def notify_to_slack_channel(token, channel_id, message_as_string):
    bearer_token = 'Bearer ' + token
    headers = {'Accept': 'application/json',
               'Content-type': 'application/json', 'Authorization': bearer_token}
    slack_post_message_url = 'https://slack.com/api/chat.postMessage'
    message_body = {'channel': channel_id, 'text': message_as_string}
    try:
        print('push slack notification to channel_id: ' + channel_id)
        requests.post(slack_post_message_url, headers=headers, data=json.dumps(message_body))

    except Exception as e:
        print('slack notification failed ' + e)


# perform health-check on a given url every 5 seconds
if __name__ == '__main__':
    print('started health-check listener for: ' + service_url)
    while True:
        try:
            response = requests.get(service_url)
            status_code = response.status_code
            if status_code != 200:
                raise Exception
            print('service is healthy')
            time.sleep(5)
        # i kept it generic for simplicity,
        # for a production-grade application i would handle exceptions based on their implications
        # alongside meaningful logs
        except Exception:
            print('service is down')
            notify_to_slack_channel(auth_token, slack_channel_id, default_message)
            break
