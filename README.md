# HTML to JSON Lambda Function

This project contains an AWS SAM template that deploys a Lambda function. The function is triggered by an S3 event when a new HTML file is uploaded to a specific S3 bucket. The function then converts the HTML to JSON using the `html_to_json` library and saves the JSON to a different S3 bucket.

## Deployment

1. Review the SAM template "template.yaml" and modify the parameters as needed. This template requires you to create 2 S3 buckets, one for the HTML files and one for the JSON files. You can also modify the Lambda function's memory size, timeout, and other parameters.

2. Build the SAM application:

```bash
sam build
```

3. Deploy the SAM application:

```bash
sam deploy --guided
```

Follow the prompts in the deploy process to specify the stack name and region. You can also specify advanced options, such as whether to allow SAM CLI to create IAM roles for you.(Required)

Usage
Upload an HTML file to the S3 bucket specified in the SAM template. The Lambda function will be triggered, convert the HTML to JSON, and save the JSON to the specified S3 bucket.
