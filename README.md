### sam-github-webhook-handler

![alt text](https://github-cf.sourabh.org/images/Github-webhook-handler_v2.png)

This is a production ready github webhook handler built and deployed using AWS SAM.
API-GW -> Lambda combination gives us an API capable of handling any POST requests sent by the Github Webhook.
This Lambda function in-turn publishes to an SNS Topic and the idea is to subscribe any action listener on this topic.
I am subscribing a sample Lambda data-processor for reference.

Pre-requisites:
* AWS Account
* SAM CLI
* Python
* Docker

Steps to run and deploy:
* git clone
```
git clone https://github.com/soumoks/sam-github-webhook-handler.git
```

* Build the application
```
sam build -t sam_template.yaml
```

* Test locally
```
sam local invoke GithubHandlerFunction
```

* Package the application
```
sam package --template-file sam_template.yaml --output-template-file packaged.yaml --s3-bucket <s3_bucket_name>
```

* Deploy
```
sam deploy --template-file packaged.yaml --stack-name github-handler-api --capabilities CAPABILITY_NAMED_IAM --region us-east-1
```




