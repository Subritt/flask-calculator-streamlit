from flask import Flask, request, jsonify

app = Flask(__name__)

print(__name__)

@app.route('/')
def home():
    return 'welcome!'

@app.route('/calculate', methods=['GET'])
def calculate():
    print('\nentered calculate method\n')

    operation = request.form['operation']
    number1 = float(request.form['number1'])
    number2 = float(request.form['number2'])

    print(f'\n{{ \n    operation -> {operation}, \n    number1 -> {number1}, \n    number2 -> {number2} \n}}\n')

    if operation == 'Addition':
        result = number1 + number2
    elif operation == 'Subtraction':
        result = number1 - number2
    elif operation == 'Multiplication':
        result = number1 * number2
    elif operation == 'Division':
        result = number1 / number2
    else:
        result = 'enter the correct operation code'
    
    print(f'\n{operation}: \nnumber1 = {number1}, number2 = {number2}\nresult = {result}\n')

    # return f'{operation}: \nnumber1 = {number1}, number2 = {number2}\nresult = {result}'
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(port=8000)
