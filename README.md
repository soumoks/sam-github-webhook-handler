### sam-github-webhook-handler

![alt text](https://github-cf.sourabh.org/images/Github-webhook-handler_v2.png)

This is a production ready github webhook handler built and deployed using [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).

API-GW -> Lambda combination gives us an API capable of handling any POST requests sent by the Github Webhook.
This Lambda function in-turn publishes to an SNS Topic and the idea is to subscribe any action listener on this topic.
I am subscribing a sample Lambda data-processor for reference.

Why is SNS used in this architecture?
[SNS](https://aws.amazon.com/sns/) is used to decouple the github-handler Lambda function from the event-processor. 
This lets the github-handler Lambda function respond to the webhook without waiting on the event-processor's response.

Use-cases:
* Trigger a CI/CD Pipeline on git push/pull_request
* Run unit tests/integration tests
* Run static code analysis/Linting
* Trigger workflows within AWS Cloud/on-premises

Pre-requisites:
* [AWS Account](https://portal.aws.amazon.com/billing/signup)
* [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3.6+](https://www.python.org/)
* [Docker](https://www.docker.com/products/docker-desktop)

Steps to run and deploy:
* Clone the repository
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

The above command returns an API endpoint that can be configured as a github webhook.
Configure accordingly.

![alt text](https://github-cf.sourabh.org/images/webhook_1_edit.png)


For additional information on github webhooks, please refer to the official [documentation](https://developer.github.com/webhooks/).