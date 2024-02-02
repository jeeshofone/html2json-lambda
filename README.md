# HTML to JSON Lambda Function

This project contains a AWS CloudFormation template that deploys a Lambda function. The function is triggered by an S3 event when a new HTML file is uploaded to a specific S3 bucket. The function then converts the HTML to JSON using the `html2json` library and saves the JSON to a different S3 bucket.

## Deployment

1. Update the CloudFormation template (`template.yaml`) with your specific AWS account ID, Lambda execution role, and the name of the S3 bucket where the JSON files will be stored.

2. Deploy the CloudFormation stack using the AWS CLI:

```bash
aws cloudformation deploy --template-file /path_to_your_template/template.yaml --stack-name YourStackName
```

## Usage

Upload an HTML file to the S3 bucket specified in the CloudFormation template. The Lambda function will be triggered, convert the HTML to JSON, and save the JSON to the specified S3 bucket.