#!/usr/bin/env python
__import__(#needed for Heroku:
  #check if a part is defined in an env variable(e.g. by Heroku)
  #otherwise set to 5000(local host)
  #define the host is also needed
myPort = int(os.environ.get("PORT",5000))
app.run(host='0.0.0.0',debug=True,port=myPort))
http://localhost:8888/