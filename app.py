import boto3

def create_my_stack():

    client = boto3.client('cloudformation')

    stack_name = "test-stack"
    stack_template = "https://s3.amazonaws.com/test-bucket/iam-role.yml"

    response = client.create_stack(
        StackName=stack_name,
        TemplateURL=stack_template,
        Parameters=[
            {
                'ParameterKey': 'MyRoleName',
                'ParameterValue': 'sample-test-role'
            },
        ]
    )
    print(response)

    return True


def update_my_stack():
    """
    Bug :
        If I'm passing 'UsePreviousTemplate': True, instead of TemplateBody or TemplateURL :
            The error message "Unable to get template body from input" is raised
        If I change my code to use TemplateURL instead, it works perfectly fine.
    """

    client = boto3.client('cloudformation')

    stack_name = "test-stack"
    # stack_template = "https://s3.amazonaws.com/test-bucket/iam-role.yml"

    response = client.update_stack(
        StackName=stack_name,
        UsePreviousTemplate=True,
        # TemplateURL=stack_template,
        Parameters=[
            {
                'ParameterKey': 'MyRoleName',
                'ParameterValue': 'sample-test-role-new'
            },
        ]
    )
    print(response)

    return True
