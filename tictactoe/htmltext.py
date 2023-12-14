

def htmlfile(board):
    html = """
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
    <h1>"""+board+"""
    </h1>
    </body>
    </html>
    """
    return html
    
def htmlnoinfo():
    html = """
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
    <h1> Please input password or userid</h1>
	<form action="https://okwcbra4u6.execute-api.us-east-1.amazonaws.com/tictactoe/Tictactoe" method="get">
    <lable for="user_id">Enter UserID</lable>
    <input type="text" id="user_id" name="user_id"></br>
    <lable for="password">Enter Password</lable>
    <input type="text" id="password" name="password"></br>
    <input type="submit" value="Submit" value:"Log In">
    </form>
    <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/">
	<input type="submit" value="Main Page">
	</form>


</body>
</html>
    """
    return html
    
def htmlwrongpassword():
    html = """
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
    <h1>Please input correct password</h1>
	<form action="https://okwcbra4u6.execute-api.us-east-1.amazonaws.com/tictactoe/Tictactoe" method="get">
    <lable for="user_id">Enter UserID</lable>
    <input type="text" id="user_id" name="user_id"></br>
    <lable for="password">Enter Password</lable>
    <input type="text" id="password" name="password"></br>
    <input type="submit" value="Submit" value:"Log In">
    </form>
    <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/">
	<input type="submit" value="Main Page">
	</form>


</body>
</html>
    """
    return html
    
def htmlinput(board,user_id,password):
    html = """
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
    <h1>"""+board+"""
    </h1>
    <form action="https://okwcbra4u6.execute-api.us-east-1.amazonaws.com/tictactoe/Tictactoe" method="get">
    	<lable for="userinput"> Please select your move with number 1-9</lable>
        <input type="text" id="userinput" name="userinput"></br>
        <input type="hidden" id="user_id" name="user_id" value="""+user_id+""" >
        <input type="hidden" id="password" name="password" value="""+password+""" >
        <input type="submit" name = "SUBMIT" value:"Submit Turn">
    </form>
    <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/userlogin.html?">
    <input type = "submit" value = "Return to log in">
    </form>
    
    <form action="https://okwcbra4u6.execute-api.us-east-1.amazonaws.com/tictactoe/Tictactoe" method="get">
        <input type="hidden" id="reset" name="reset" value = "true">
        <input type="hidden" id="user_id" name="user_id" value="""+user_id+""" >
        <input type="hidden" id="password" name="password" value="""+password+""" >
        <input type="submit" name = "SUBMIT" value = "reset board">
    </form>
    <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/">
	<input type="submit" value="Main Page">
	</form>
    
    </body>
    </html>
    """
    return html
    
def htmlplayerwin(board,winner,user_id,password):
    html = ""
    if winner == 1:
        html = """
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
        <h1>"""+user_id+""" wins</h1>
    
        <h1>"""+board+"""
        </h1>
        <form action="https://okwcbra4u6.execute-api.us-east-1.amazonaws.com/tictactoe/Tictactoe" method="get">
    	<lable for="userinput">Do you want to reset the game? </lable>
        <input type="hidden" id="reset" name="reset" value = "true">
        <input type="hidden" id="user_id" name="user_id" value="""+user_id+""" >
        <input type="hidden" id="password" name="password" value="""+password+""" >
        <input type="submit" name = "SUBMIT" value:"Play Again?">
        </form>
        <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/userlogin.html?">
        <input type = "submit" value = "Return to log in">
        </form>
        <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/">
	    <input type="submit" value="Main Page">
	    </form>
        </body>
        </html>
        """
    elif winner == 3:
        html = """
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
        <h1>Its a Tie</h1>
    
        <h1>"""+board+"""
        </h1>
        <form action="https://okwcbra4u6.execute-api.us-east-1.amazonaws.com/tictactoe/Tictactoe" method="get">
    	<lable for="userinput">Do you want to reset the game? </lable>
        <input type="hidden" id="reset" name="reset" value = "true">
        <input type="hidden" id="user_id" name="user_id" value="""+user_id+""" >
        <input type="hidden" id="password" name="password" value="""+password+""" >
        <input type="submit" name = "SUBMIT" value:"Play Again?">
        </form>
        <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/userlogin.html?">
        <input type = "submit" value = "Return to log in">
        </form>
        <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/">
	    <input type="submit" value="Main Page">
	    </form>
        </body>
        </html>
        """
    else:
        html = """
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
        <h1>The Bot wins</h1>
     
        <h1>"""+board+"""
        </h1>
        <form action="https://okwcbra4u6.execute-api.us-east-1.amazonaws.com/tictactoe/Tictactoe" method="get">
        <lable for="userinput">Do you want to reset the game? </lable>
        <input type="hidden" id="reset" name="reset" value = "true">
        <input type="hidden" id="user_id" name="user_id" value="""+user_id+""" >
        <input type="hidden" id="password" name="password" value="""+password+""" >
        <input type="submit" name = "SUBMIT" value:"Play Again?">
        </form>
        <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/userlogin.html?">
        <input type = "submit" value = "Return to log in">
        </form>
        <form action="http://gabriel-awsprojects.s3-website-us-east-1.amazonaws.com/">
	    <input type="submit" value="Main Page">
	    </form>
        </body>
        </html>
        """
    return html
