from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api=Api(app)

class Less_Than(Resource):
    def get(self,n1,n2):
        if(n1<n2):
            return str("True")
        else:
            return str("False")
       

api.add_resource(Less_Than, '/<n1>/<n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5058,
        host="0.0.0.0"
    )
