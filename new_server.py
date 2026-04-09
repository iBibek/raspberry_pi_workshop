from flask import Flask, render_template_string, request, redirect, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
led_state = False

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>LED Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background: #1a1a2e;
        }
        .container { text-align: center; }
        h1 { color: white; margin-bottom: 30px; }
        .btn {
            padding: 20px 60px;
            font-size: 24px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            color: white;
            transition: background 0.3s;
        }
        .btn-on { background: #e94560; }
        .btn-on:hover { background: #c81e45; }
        .btn-off { background: #0f3460; }
        .btn-off:hover { background: #16213e; }
        .status {
            color: #aaa;
            margin-top: 20px;
            font-size: 18px;
        }
        .dot {
            display: inline-block;
            width: 12px; height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .dot-on { background: #00ff88; box-shadow: 0 0 10px #00ff88; }
        .dot-off { background: #555; }
    </style>
</head>
<body>
    <div class="container">
        <h1>LED Control</h1>
        <a href="/toggle">
            <button class="btn {{ 'btn-on' if state else 'btn-off' }}">
                {{ 'Turn OFF' if state else 'Turn ON' }}
            </button>
        </a>
        <div class="status">
            <span class="dot {{ 'dot-on' if state else 'dot-off' }}"></span>
            LED is {{ 'ON' if state else 'OFF' }}
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML, state=led_state)

@app.route("/toggle")
def toggle():
    global led_state
    led_state = not led_state
    GPIO.output(18, GPIO.HIGH if led_state else GPIO.LOW)
    return render_template_string(HTML, state=led_state)

@app.route("/led")
def led_control():
    global led_state
    state_param = request.args.get("state", "").lower()
    if state_param in ("on", "1", "true"):
        led_state = True
        GPIO.output(18, GPIO.HIGH)
    elif state_param in ("off", "0", "false"):
        led_state = False
        GPIO.output(18, GPIO.LOW)
    return render_template_string(HTML, state=led_state)

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        GPIO.cleanup()