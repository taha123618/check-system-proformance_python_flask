from flask import Flask, render_template
import psutil
app = Flask(__name__)


@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_precent = psutil.virtual_memory().percent
    Message = None

    if cpu_metric > 80:
        Message = "High CPU scale up!!!"
    if mem_precent > 80:
        Message = "High Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_metric, mem_precent=mem_precent, Message=Message)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
