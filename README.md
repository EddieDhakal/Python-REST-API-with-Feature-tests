#Ticketing System Backend

##Intro

A simple demonstration of a REST API in Python with Feature tests.

*Please Note: This is a demonstration of a REST API rather than an issue tracking system.

#Sample Requests and Responses

###Create ticket request

```
{
    "type": "Bug"
    "message": "The links are broken."
}
```

###Create ticket response

```
{
    "id": 123456,
    "type": "Bug",
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
    "type": "Bug",
    "status": "closed"
}
```