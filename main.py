# External Flask imports
from flask import Flask, render_template, make_response, send_from_directory, json, request
from flask_restful import Api, Resource

# This is our own module used for using our system
from system.Platform import Platform

# This will create a Flask Application on the base URL i.e. "http://localhost", "http://10.10.10.6"
app = Flask(__name__, static_url_path='')
# We hand our Flask Application to flask_restful to ease the development of our REST api
api = Api(app)

# Here we create a Platform Object which is our own system
platform = Platform()

# This block handles serving static content made available on the assets
# directory. This is typically things like images, external JS and CSS.
@app.route('/assets/<path:path>')
def send_js(path):
    print(path)
    return send_from_directory('assets/', path)

### REST Endpoint Classes
# UI is the Class we attach to the base url to control our HTTP request
class UI(Resource):
    # To utilize flask_restful we create functions named by the HTTP request
    # we would like to attach to on that URL. i.e. get, post, put, etc (Case Sensitive)
    def get(self):
        # This section generates an html page to send to the client when they visit
        # the webapp
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html',
            aVoltage=str(platform.get_aVoltage()) + " V",
            tVoltage=str(platform.get_tVoltage()) + " V",
            oVoltage=platform.get_oVoltage(),
            manufacturer="CAEN",
            serial_number=platform.get_sn(),
            type="HPGe"), 200,headers)

# This is the class we attach to setvoltage to control the voltage of our system
class SetVoltage(Resource):
    def post(self):
        # Creates a dictionary of the JSON we recieve from the client
        json_dict = request.get_json()
        # Using our platform we set the target voltage of the system
        platform.set_tVoltage(json_dict['setVoltage'])
        # Construction of a response back to the client to let them know we did it
        headers = {"Content-Type": "application/json"}
        return make_response(json.dumps({'Well': 'Does it work?',
        'Ayyy': 'It should have'}), 200, headers)

### Attaching REST Classes to urls
api.add_resource(UI, '/')
api.add_resource(SetVoltage, '/setvoltage')

### We execute the following if we call the script directly
if __name__ == '__main__':
    ## We attach to all devices on the Pi on port 80 (Default http port)
    app.run(host='0.0.0.0', port=80)
