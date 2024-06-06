import boto3
from fastapi import HTTPException
from pydantic import EmailStr
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(['html', 'xml'])
)

# Initialize AWS SES client
ses_client = boto3.client(
    'ses',
    region_name=os.getenv('AWS_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)


def send_email_register(user):
    print(user)
    template = env.get_template("register.html")
    html_content = template.render(name=user.name)
    send_email(user.email, 'Registered successfully', html_content)


def send_email(email: EmailStr, subject: str, content: str):
    try:
        response = ses_client.send_email(
            Source=os.getenv('EMAIL_ADMIN'),
            Destination={
                'ToAddresses': [email],
            },
            Message={
                'Subject': {
                    'Data': subject,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Html': {
                        'Data': content,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )
        return {"message": "Email sent successfully", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
