import logging
import json

#logger config
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    This Lambda function is invoked by AWS SNS on a git push
    """
    logger.info("Received notification from SNS")
    logger.info(json.dumps(event,indent=4))    
    logger.info("Message processed!")
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        }
        # "body": json.dumps(event, indent=4),
    }
