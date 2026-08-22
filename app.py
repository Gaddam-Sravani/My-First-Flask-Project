from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
	return """
	<html>
		<body>
			<h1> My Web Application is Live </h1>
		</body>
	</html>"""
if __name__== "__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)

