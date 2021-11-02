from flask import *
import os
import subprocess
from werkzeug.utils import secure_filename
from random import randint


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		# list files in current directory
		p = subprocess.Popen(["ls", "-a"], stdout=subprocess.PIPE)
		out, err = p.communicate()
		return out
	else:
		# get the file uploaded
		file = request.files['file']

		print(f"[+] {request.remote_addr} try to upload {file.filename}")

		if file.filename != '':
			if os.path.exists(file.filename):
				new_filename = file.filename + "_" + str(randint(0,999999))
				filename = secure_filename(new_filename)
				file.save(os.path.join(".", filename))

				return f"The file already exists, is was renammed as {new_filename}"
			else:
				filename = secure_filename(file.filename)
				file.save(os.path.join(".", filename))

				return "File uploaded!"
		else:
			return "Filename can't be null"

    

# Download file content
@app.route("/<filename>")
def download(filename):
	filename = escape(filename)

	if ".." not in filename:
		if os.path.exists(filename):
			msg = open(filename).read()
		else:
			msg = f"{filename} dont exists"

	return msg

app.run(host="0.0.0.0")
