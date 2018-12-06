from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api, Resource, fields

#local import
from app.models import Incident, IncidentSchema, incident_list

incident_Schema = IncidentSchema()
incidents_Schema = IncidentSchema(many=True)

class MyIncidents(Resource):
    def __init__(self):
        super(MyIncidents, self).__init__()

    def get(self):
        incidents = incidents_Schema.dump(incident_list).data
        return jsonify({"status": 200, "data": [{"incidents": incidents, "message" : "successfully fetched all records"}]})
    
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return jsonify({'status':200, 'message': 'no input data provided'})
        # Validate and deserialize input 
        data, errors = incident_Schema.dump(json_data)
        if errors:
            return jsonify({"status": 422, "data": errors})
        elif not data['comment']:
            return jsonify({"status": 200, "data": [{"message" : "please comment on the incident you would like to report"}]})
        new_incident = Incident(
            createdBy = data['createdBy'],
            type_of_incident = data['type_of_incident'],
            location = data['location'],
            status = data['status'],
            images = data['images'],
            videos = data['videos'],
            comment = data['comment']
            )
        
        incident_list.append(new_incident)
        result = incident_Schema.dump(new_incident).data
        return jsonify({'status': 200, 'data': [{"id" : result['id'], "message" : "created red flag record" }]})

class MyIncident(Resource):
    def __init__(self):
        super(MyIncident, self).__init__()

    def get(self, id):
        if 0 < id <= len(incident_list):
             incident = incident_Schema.dump(incident_list[id-1]).data
             return jsonify({"status": 200, "data": [incident]})
        abort(404)
        

    def put(self, id):
        incident = incident_Schema.dump(incident_list[id-1]).data
        json_data = request.get_json(force=True)
        if not json_data:
               return jsonify({'status':200, 'message': 'no input data provided'})
        # Validate and deserialize input
        data = incident_Schema.dump(json_data).data
        for key in data.keys():
            if data[key] is not None:
                incident[key] = data[key] 

        updated_incident = incident_Schema.load(incident).data
        incident_list[id-1] = updated_incident

        result = incident_Schema.dump(incident).data
        

        return jsonify({'status': 200, 'data': [{"id" : result['id'], "message" : "updated red flag record" }]})

    def delete(self, id):
        incident = incident_list[id-1]
        incident_list.remove(incident)
        
        result = incident_Schema.dump(incident).data
        return jsonify({"Status": 200, "data": [{"id" : result['id'], "message" : "deleted a red flag record" }]})