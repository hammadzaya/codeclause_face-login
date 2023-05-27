import json
import boto3

def lambda_handler(event, context):
  
    ssm_client = boto3.client('ssm', region_name='ap-south-1')
    
    cmd = { "commands": [ "sudo usermod -L HAmmad" ] }
    
    ssm_client.send_command(DocumentName="AWS-RunShellScript", InstanceIds=["i-0b1b5389145225917"], Parameters=cmd )
    
    return {
        'statusCode': 200,
        'body': json.dumps('User Locked!')
    }
