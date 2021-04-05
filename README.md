# simple-api

This API simply returns JSON objects stored in a DynamoDB table. The API is available at http://simple-api-210961460.eu-west-1.elb.amazonaws.com.
Use `curl` or your favorite browser to perform the requests. 
#### Available endpoints
* Get all elements: `GET /api/v1/resources/questions/all`
* Get element by ID: `GET /api/v1/resources/questions?id=[1-15]`