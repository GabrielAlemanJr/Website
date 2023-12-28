import boto3
import json
import os
import cfnresponse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("this is event -> "+str(event))
    print("this is context -> "+str(context))
    userlogin = userloginfile()
    randomNumber = randomnumber()
    key = ['website.html']    
    destination_bucket = os.environ["BucketName"]
    for x in key:
        source = {'Bucket': 'gabriel-awsprojects', 'Key': x}
        response = s3.copy(source, destination_bucket, x)
    s3.put_object(Bucket=destination_bucket,Key="userlogin.html",Body=userlogin,ContentType ="text/html")
    s3.put_object(Bucket=destination_bucket,Key="RandomNumber.html",Body=randomNumber,ContentType ="text/html")
    cfnresponse.send(event, context, cfnresponse.SUCCESS,{})

def randomnumber():
  randomapi = os.environ["RandomApi"]
  urlbucket = os.environ["urlbucket"]
  http = """
    <!doctype html>
    <html lang="en">
    <style>
    input[type=submit]{
      text-align: center;
      font-size: 16px;
      margin: 6px 6px;
      cursor: pointer;
    }


    </style>
        <body style="background-color:white;">
      <h1> This is Random Generator</h1>
      <form action=" """ + randomapi + """ " method="get">
        <label for="min">Enter Min Value:</label>
      <input type="text" id="min" name="min" value="1">
      <label for="max">Enter Max Value:</label>
      <input type="text" id="max" name="max" value="10"></br>
      <input type="submit" value="Submit">
      </form>

      <form action=" """+urlbucket+""" ">
      <input type="submit" value="Main Page">
      </form>
      
      </body>
      </html>
  """
  return http

def userloginfile():
  test = os.environ["ApiUrl"]
  urlbucket = os.environ["urlbucket"]
  http = """
  <!DOCTYPE html>
  <html>
  <style>
    @media(max-width: 1000px){
        form{
          width:750px;   
          text-alignment:center;
            margin:0 auto;
            background:white;
              padding-right:25px;
          }
          h1{
          font-size: clamp(60px,3vw,100px);
          text-align:center;
          }
          
          input[type=submit]{
          background-color:orange;
          width: 100%;
          text-align:center;
          font-size: clamp(30px,3vw,40px);
            margin:6px 10px;
            cursor: pointer;
          }
          input[type=text]{
    
          width:725px;
          text-align: left;
          font-size: clamp(30px,3vw,40px);
          margin:6px 10px;
          cursor: pointer;
          }
          lable{
          width: 300px;
          display:block;
          font-size: clamp(30px,3vw,40px);
          margin: 6px 6px;
            cursor: pointer;
          }
    body {
      background-color: lightgray;
          }
    }

    @media(min-width: 1000px){
        form{
          width:750px;   
          text-alignment:center;
            margin:0 auto;
            background:white;
              padding-right:25px;
          }
          h1{
          font-size: clamp(60px,3vw,100px);
          text-align:center;
          }
          
          input[type=submit]{
          background-color:orange;
          width: 100%;
          text-align:center;
          font-size: clamp(30px,3vw,40px);
            margin:6px 10px;
            cursor: pointer;
          }
          input[type=text]{
    
          width:750px;
          text-align: left;
          font-size: clamp(30px,3vw,40px);
          margin:6px 10px;
          cursor: pointer;
          }
          lable{
          width: 300px;
          display:block;
          font-size: clamp(30px,3vw,40px);
          margin: 6px 6px;
            cursor: pointer;
          }
    body {
      background-color: lightgray;
          }
    }
          </style>
  <body>
    <form action=" """ + test + """ " method="get">
      <lable for="user_id">Enter UserID</lable>
      <input type="text" id="user_id" name="user_id"></br>
      <lable for="password">Enter Password</lable>
      <input type="text" id="password" name="password"></br>
      <input type="submit" value="Log In">
      </form>
      <form action=" """+urlbucket+""" ">
      <input type="submit" value="Main Page">
      </form>


  </body>
  </html>
  """
  return http
