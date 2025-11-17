from flask import Flask, request, jsonify
from database import SessionLocal, Turbidity
from datetime import datetime

app = Flask(__name__)

@app.route("/api/turbidity", methods=["POST"])
def receive_turbidity():
    json_data = request.get_json(force=True)

    session = SessionLocal()
    turbine = Turbidity(
        device_id=json_data.get("device_id"),
        raw=json_data.get("turbidity_raw"),
        ntu=json_data.get("turbidity_ntu"),
        timestamp=datetime.now()
    )
    session.add(turbine)
    session.commit()
    session.close()

    return jsonify({"status": "ok"}), 200


@app.route("/api/turbidity/all")
def get_all():
    session = SessionLocal()
    rows = session.query(Turbidity).all()
    session.close()

    return jsonify([
        {
            "id": r.id,
            "device_id": r.device_id,
            "raw": r.raw,
            "ntu": r.ntu,
            "timestamp": r.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        for r in rows
    ])

@app.route("/")
def home():
    return "Server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
    