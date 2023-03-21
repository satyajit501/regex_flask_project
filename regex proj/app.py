from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the test string and regular expression from the form
        test_string = request.form['test_string']
        regex = request.form['regex']
        
        # Find all the matches
        matches = re.findall(regex, test_string)
        
        # Render the results template with the matched strings
        return render_template('results.html', matches=matches)
    
    # If the request method is GET, just render the index template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
