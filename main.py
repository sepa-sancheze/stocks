from app.AWSConnections import AWSConnections

aws = AWSConnections()
awsSession = aws.getSession()

def saveUserDynamoDB(session, user):
  dynamodb = session.resource('dynamodb')
  table = dynamodb.Table('Users')
  response = table.put_item(Item=user)
  return response

saveUserDynamoDB(awsSession, {"email": "jose@correo.com", "dpi": "123"})