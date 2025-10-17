import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'Please enter something'

    if request_json and 'cholesterol' in request_json:
        cholesterol_value = request_json['cholesterol']
    elif request_args and 'cholesterol' in request_args:
        cholesterol_value = request_args['cholesterol']
    try: 
        cholesterol_value = float(cholesterol_value)
    except (TypeError, ValueError):
        return 'You messed up'

    if 200 <= cholesterol_value <= 239:
        cholesterol_value_label = 'At risk'
    elif cholesterol_value >= 240:
        cholesterol_value_label = 'Dangerous'
    else:
        cholesterol_value_label = 'Heart Healthy'
    
    return cholesterol_value_label
