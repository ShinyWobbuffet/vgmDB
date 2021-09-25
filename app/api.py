from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def main():
  return {"res": 0}

@app.route("/<hash>")
def view(identifier):
  file = open("data.json")
  data = file.read()

  if data.games[identifier]:
    return {"res": data.games[identifier]}
  elif data.songs[identifier]:
    return send_file("../vgm/" + data.songs[identifier])
  else:
    return {"res": -1}
