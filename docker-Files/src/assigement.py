from flask import Flask , jsonify , render_template
import socket
application=app=Flask(__name__)

def fetchdetalis():
	hostname=socket.gethostname()
	host_ip=socket.gethostbyname()
	return str(hostname), str(host_ip)

@app.route("/")
def hello():
	return "<p>hello world</p>"

@app.route("/health")
def health():
	return jsonify(
		status= "up"
    )

@app.route("/details")
def details:
	hostname , ip = fetchdetails()
	return render_template('index.html',HOSTNAME=hostname , IP=ip)


if __name__== '__main__'
	app.run(host='0.0.0.0',port=5000)