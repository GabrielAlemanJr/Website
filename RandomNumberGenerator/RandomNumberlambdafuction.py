import json
import random

def lambda_handler(event, context):
    #gets min and max from the webpage and checks if its numbers, min<=max, and then selects a random numebr between the range
    message = ''
    min = 0
    max = 0
    min = event.get('queryStringParameters').get('min')
    max = event.get('queryStringParameters').get('max')
    if False==min.isnumeric() or False==max.isnumeric():
        message = 'Input only numbers'
    elif min>max:
        message = 'Min is smaller than max'
    else:
        message = random.randint(int(min),int(max))
        
    #html document displaying the random number and a button to return to main page    
    html="""
    <!DOCTYPE html>
    <html>
    <style>
    input[type=submit]{
     text-align: center;
     font-size: 16px;
     margin: 6px 6px;
     cursor: pointer;
    }
    </style>
    <body>
    <h1>"""+str(message)+"""</h1>
    <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com">
    <input type="submit" value="Return to Main Page">
    </form>
    <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/RandomNumber.html?">
    <input type="submit" value="Return to Random Number Generator">
    </form>
    </body>
    </html>
    """
        
    return {
        'statusCode': 200,
        'body': html,
        "headers":{
            'Content-Type': 'text/html',
        }
    }
