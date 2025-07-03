# 🧮 Serverless Number Analysis API

A fully serverless API built with AWS Lambda, API Gateway, and DynamoDB.  
Takes in a number and returns whether it's even and/or prime — then logs the result with a timestamp.

## 🛠️ Stack

- **Language**: Python 3.11
- **API**: AWS API Gateway (HTTP + POST)
- **Compute**: AWS Lambda
- **Database**: DynamoDB (NoSQL)
- **Infrastructure-as-Code**: AWS SAM (Serverless Application Model)

## 📦 Features

- ✅ Accepts JSON POST requests with a `number`
- ✅ Checks if the number is even or prime
- ✅ Logs the number and results to DynamoDB with UUID and timestamp
- ✅ Fully deployable via `sam deploy`

## 📥 Sample Request

```bash
curl -X POST https://your-api-url.amazonaws.com/Prod/hello/ \
  -H "Content-Type: application/json" \
  -d '{"number": 42}'
