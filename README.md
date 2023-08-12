### Basic Calculator

This basic calculator covers the concept of creating a flask api, and streamlit for frontend.

#### Technologies used:
- `Flask` is used to handle the backend. Calculator (Addition, Subtraction, Multiplication, Division) logic is written on the backend. This API accepts a form data consisting of the following and returns a json output `result`.
    - `Operation`, which operation to perform.
    - `number1`, first number for the operation.
    - `number2`, second number for the operation.
- `Streamlit` is used to handle the frontend. Two number input fields, and one Operation dropdown has been created for the user to interact, and whenever they click the calculate button it will show the result from the inputs given.
- `AWS Elastic Beanstalk`, [Flask backend](http://flask-calculator-api.us-east-1.elasticbeanstalk.com/) has been deployed here, which then is called from Streamlit server.
- `Streamlit`, [frontend](https://flask-calculator-app.streamlit.app/) has been deployed here, which calls the Flask backend hosted in AWS.

Below is a flow chart showing the communication between `client (Streamlit)`, and `Server (Flask)`

```mermaid
sequenceDiagram
    participant Streamlit
    participant AWS (Flask)
    Streamlit->>+AWS (Flask): Request (operation, number1, number2)
    AWS (Flask)->>-Streamlit: Response (result)
