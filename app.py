from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Pipeline Application Running!"

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "DevSecOps Pipeline"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)