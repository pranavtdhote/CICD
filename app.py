from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Version / Build Info (CHANGE THIS TO TEST CI/CD)
BUILD_VERSION = "v2 - Updated via Jenkins"

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            return "<h3 style='color:red;text-align:center;'>All fields are required!</h3>"

        return redirect(url_for('success', username=name))

    return render_template('register.html', version=BUILD_VERSION)


@app.route('/success/<username>')
def success(username):
    return f"""
    <h2 style='color:green;text-align:center;margin-top:50px;'>
    ✅ Registration Successful! Welcome {username}
    </h2>
    <p style='text-align:center;'>Build Version: {BUILD_VERSION}</p>
    """


@app.route('/health')
def health():
    return {
        "status": "OK",
        "version": BUILD_VERSION,
        "time": str(datetime.datetime.now())
    }, 200


if __name__ == '__main__':
    print(f"🚀 CI/CD Trigger Test - {BUILD_VERSION}")
    app.run(debug=False, host='0.0.0.0', port=5000)

//Testing Jenkins
