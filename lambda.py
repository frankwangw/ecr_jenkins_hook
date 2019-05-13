import jenkins


def lambda_handler(event, context):
    # TODO implement
    server = jenkins.Jenkins(JenkinsHostUrl, username='admin', password='myyellow')
    
    server.build_job(JenkinsJobName)