"""
An infinite loop causing piece of code found in our November 16th/17th 2017 evaluation
http://pyt.readthedocs.io/en/latest/past_evaluations.html#november-16-17th-2017
"""

@app.route('/recommended', methods=["GET", "POST"])
def recommended():
    if is_google_auth():
        location = get_location(http_auth)


def get_location(http_auth):
    for i in range(len(events_result['items'])):
        example = events_result['items'][i]['start']
        if 'dateTime' in example.keys():
            index_of_valid_event = i
            break
    return 5
