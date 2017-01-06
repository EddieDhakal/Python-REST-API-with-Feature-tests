#Ticketing System Backend

##Intro
A simple demonstration of a REST API in Python with Feature tests.

Please Note: This is just a simple demonstration of a REST API rather than an issue tracking system.

#Sample Requests and Responses

###Create ticket request
```
{
    "ticket_type": "Bug",
    "message": "The links are broken."
}
```

###Create ticket response
```
{
    "id": 123456,
    "ticket_type": "Bug",
    "status": "opened"
}
```

###Query ticket status request
```
{
    "id": 123456
}
```

###Query ticket status response
```
{
    "id": 123456
    "ticket_type": "Bug",
    "status": "closed"
}
```

#Dependencies
 - `behave` For testing features
 - `requests` For testing HTTP API calls
 - `oktest` For testing units
 - `falcon` REST framework
 - `cython` For accelerating falcon (optional)
 - `sqlite3` For presistance

#Dev Installation
It is recommended to use a Python virtual environment like `pyenv` or the default `virtualenv`.

`$ python setup.py develop`


##Creating database
Please make sure `sqlite3` is installed.

For example, if you are on Ubuntu `$ sudo apt-get install sqlite3` will do the job.

Then create the database
`$ cat ticket.sql | sqlite3 ticket.db`
