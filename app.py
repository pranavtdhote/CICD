from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home / Registration Route
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Safely get form data
        name = request.form.get('name')
        email = request.form.get('email')

        # Basic validation
        if not name or not email:
            return "<h3 style='color:red;text-align:center;'>All fields are required!</h3>"

        # Redirect to success page (better practice than returning raw HTML)
        return redirect(url_for('success', username=name))

    return render_template('register.html')


# Success Route
@app.route('/success/<username>')
def success(username):
    return f"""
    <h2 style='color:green;text-align:center;margin-top:50px;'>
    ✅ Registration Successful! Welcome {username}
    </h2>
    """


# Health Check Route (useful for Docker / Jenkins)
@app.route('/health')
def health():
    return {"status": "OK"}, 200


if __name__ == '__main__':
    print("🚀 CI/CD Trigger Test - Flask App Started")
    app.run(debug=True, host='0.0.0.0', port=5000)
