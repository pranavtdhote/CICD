from flask import Flask, render_template, request, redirect, url_for, jsonify
import datetime
import os

app = Flask(__name__)

# 🔥 Dynamic Build Info (CI/CD Friendly)
BUILD_VERSION = os.getenv("BUILD_VERSION", "v3 - CI/CD Enhanced")
BUILD_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 🏠 Home / Registration Route
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            return "<h3 style='color:red;text-align:center;'>All fields are required!</h3>"

        return redirect(url_for('success', username=name))

    return render_template(
        'register.html',
        version=BUILD_VERSION,
        build_time=BUILD_TIME
    )


# ✅ Success Route
@app.route('/success/<username>')
def success(username):
    return f"""
    <h2 style='color:green;text-align:center;margin-top:50px;'>
    ✅ Registration Successful! Welcome {username}
    </h2>
    <p style='text-align:center;'>Build Version: {BUILD_VERSION}</p>
    <p style='text-align:center;'>Build Time: {BUILD_TIME}</p>
    """


# ❤️ Health Check Route (for Jenkins/Docker)
@app.route('/health')
def health():
    return jsonify({
        "status": "OK",
        "version": BUILD_VERSION,
        "build_time": BUILD_TIME,
        "message": "CI/CD Pipeline Running Successfully 🚀"
    })


# 🔍 Debug Info Route (for testing Jenkins trigger)
@app.route('/info')
def info():
    return jsonify({
        "app": "Event Registration System",
        "version": BUILD_VERSION,
        "build_time": BUILD_TIME,
        "server": "Flask",
        "ci_cd": "Jenkins Integrated"
    })


# 🚀 Main Entry
if __name__ == '__main__':
    print("=" * 50)
    print(f"🚀 CI/CD DEPLOYMENT STARTED")
    print(f"📦 Version: {BUILD_VERSION}")
    print(f"⏰ Build Time: {BUILD_TIME}")
    print("=" * 50)

    app.run(debug=False, host='0.0.0.0', port=5000)
