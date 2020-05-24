import json
import boto3
import os
import logging

#logger config
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Lambda function is invoked on a git push by API GW
    """
    # logger.info(json.dumps(event,indent=4))
    #capture commits from github webhook message
    message = ""
    try:
        message = json.dumps(event['commits'])
    except:
        pass
    logger.info("publishing message to SNS topic..")
    logger.info(f"message: {message}")
    #publish message to sns topic
    publish_message(message)
    logger.info("Message published!")
    #A 200 HTTP response is required to be sent to github for the webhook to register a successful response.
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        }
        # "body": json.dumps(event, indent=4),
    }

def publish_message(message_to_publish=None):
    """
    Publish a message to SNS
    """
    #Obtain the topic arn from environment variables
    topic_arn = os.environ['topic_arn']
    logger.info(f"Target SNS Topic arn: {topic_arn}")
    client = boto3.client('sns')
    
    response = client.publish(
        TargetArn=topic_arn,
        Subject='git push',
        Message=json.dumps({'default': message_to_publish}),
        MessageStructure='json'
    )
    logger.info(f"SNS Response: {response}")