# pythontestAWS
This repository contains the code and necessary information for the AWS task assignment. The task was to create a simple REST API using AWS API Gateway, Lambda functions, and DynamoDB.

Inside, you will find the Lambda function code, the README file with URLs to the API GET and POST methods, and instructions on how to use them, including example requests.

## API Endpoints

### POST /user
Creates a new user record

**URL:**
`https://sm0orqxjv0.execute-api.us-east-1.amazonaws.com/prod/user`

**HEADERS:**

- Content-Type: application/json  
- x-api-key: YOUR_API_KEY

**USAGE EXAMPLE:**

$ curl -X POST "https://sm0orqxjv0.execute-api.us-east-1.amazonaws.com/prod/user" \
     -H "Content-Type: application/json" \
     -H "x-api-key: YOUR_API_KEY" \
     -d '{"first_name": "Bolo", "age": 25}'



### GET /user/{user_id}

**URL:**
`https://sm0orqxjv0.execute-api.us-east-1.amazonaws.com/prod/user/{user_id}`

**HEADERS:**
- x-api-key: YOUR_API_KEY


**USAGE EXAMPLE:**

curl -X GET https://sm0orqxjv0.execute-api.us-east-1.amazonaws.com/prod/user/USER_ID \  
   -H "x-api-key: YOUR_API_KEY"

## Security
To help protect the API from unauthorized use, all requests require an API key (`x-api-key`).
The API key has been shared via email with the recruiter to allow secure access to the API.
