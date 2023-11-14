# PC-Wakeup-Alert-using-AWS-Cloud
This project allows you to have a passive security mechanism for your personal computer. By setting it up properly, it will send a notification to your email everytime your pc starts.

To setup this project, you will initially need an AWS account and then follow the given steps:
1. Create a IAM role with the following permission policies
   a. AmazonAPIGatewayAdministrator
   b. AmazonSESFullAccess
   c. AmazonSNSFullAccess
   d. AmazonLambdaFullAccess
3. Verify the sender and reciever email addresses in the AWS SES.
4. Create a SNS topic and create a subscription where you need to put the destination email address (the email where you wish to recieve the emails.)
5. Now, create a lambda function with the latest python runtime (as we have written the codes in python). Make sure to change the default execution role and select the role you made above.
6. Now, navigate to AWS API Gateway and create a HTTP API. Make sure to add an integration of lambda.
7. Go to the AWS lambda and add the trigger as API gateway and the destination as SNS.
8.  Make the necessary changes in awslambda.py and pc.py 
9. Now, put the code of awslambda.py to the code section of the AWS lambda and deploy the changes.
10. Now, you can run the pc.py and you will recieve an email from AWS.
11. To make it send emails whenever to turn on the pc, you have to create a VBscript file with the given content.
12. Press 🪟+r and then type "shell:startup" and press enter.
13. Paste the VBscript file over here and restart your pc while the aws lambda, sns, ses, api gateway are running.
14. You will get two notifications, one from ses that your pc has been activated and the other from sns stating all the details of sending the notification.
