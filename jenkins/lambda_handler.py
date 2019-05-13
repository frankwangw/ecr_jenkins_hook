import jenkins




def lambda_handler(event, context):
    # TODO implement
    server = jenkins.Jenkins('http://10.66.37.204:8080', username='admin', password='myyellow')
    user= server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
    jobs = server.get_jobs()
    print jobs