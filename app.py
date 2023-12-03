from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    html = """
    <html>
        <body>
            <h1>Welcome!</h1>
        </body>
    </html>
    """
    return html

@app.route('/welcome/home')
def welcome_home():
       html = """
       <html>
         <body>
            <h1>Welcome home!</h1>
            <p>This is the welcome page</p>
         </body>
       </html>
       """
       return html

@app.route('/welcome/back')
def welcome_back():
       html = """
       <html>
         <body>
            <h1>Welcome back!</h1>
         </body>
       </html>
       """
       return html

@app.route('/add')
def add(a, b):
    """Add a and b."""
    a = float(request.args.get('a', 0))  
    b = float(request.args.get('b', 0))  
    result = add(a, b)
    return str(result)

@app.route('/sub')
def sub(a, b):
    """Substract b from a."""
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def mult(a, b):
    """Multiply a and b."""
    a = float(request.args.get('a', 1))  
    b = float(request.args.get('b', 1))  
    result = mult(a, b)
    return str(result)

@app.route('/div')
def div(a, b):
    """Divide a by b."""
    a = float(request.args.get('a', 1))
    b = float(request.args.get('b', 1))
    result = div(a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)