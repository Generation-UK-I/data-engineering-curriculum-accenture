# AWS Exercises

## EC2

You're going to setup your own EC2 server, then extend it so that we can host a basic website on it. After that we will look at how we can tighten security of our instances.

Before beginning, make sure the region dropdown at the top of the screen is set to Ireland (eu-west-1).

### Security Group Setup

Before creating your own EC2 instance, you will need to create a [security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html). Security groups take control of the traffic that is allowed in and out of your instance. You can apply restrictions on port ranges and IP ranges. We will be restricting `SSH` access to your IP, but open `HTTP` to the world. This is bad practice, and so you would normally be much more restrictive in terms of what you allow in and out, but for the sake and simplicity of this exercise, we won't need to worry about that.

1. Go to `EC2` page by using the search bar
1. On the left-hand side under `Network & Security`,
    1. select `Security Groups`
    1. and then select `Create security group`
1. Give your security group a unique name (e.g. `your-name-sg`) and a description (e.g. `Your-Name SG`)
1. Change the VPC to the `RedshiftVPC`
    1. Delete the contents of the `VPC` box - it should then offer you a dropdown list - select `RedshiftVPC`
    1. If not, type `Red` in the box - it should find the one named `RedshiftVPC`
1. Under `Inbound rules`, select `Add rule`
    1. Rule 1: Select `SSH` for `Type` and `My IP` for `Source`
    1. Rule 2: Select `HTTP` for `Type` and input `0.0.0.0/0` in the text field to the right of `Source` and `Anywhere-IPv4` for `Source`
1. Under `Outbound rules`,
    1. Rule 1: Select `HTTP` as the type and input `0.0.0.0/0` in the text field to the right of `Destination`
    1. Rule 2: Select `HTTPS` as the type and input `0.0.0.0/0` in the text field to the right of `Destination`
1. Under the Tags section add a tag with key `Name` and value `your-name-sg`
1. Select `Create security group` to finish

### EC2 Instance Setup

Now let's set an instance up.

1. Go to EC2 and select `Launch Instance`
1. In the `Names and tags` section,
    1. add a name for your EC2 instance ( e.g `Your-Name Web Server`)
1. In the `Application and OS Images` section,
    1. select `Amazon Linux 2023 AMI`
1. In the `Instance type` section,
    1. select an instance type of `t2.micro`
1. In the `Key pair` section,
    1. Click on the `Create new key pair` link, a pop up dialogue will appear
    1. Do so by entering a key pair name (e.g  `yourname-key`)
    1. Keep key file format as .pem and click the `Create key pair` button
    1. The key will download automatically to you downloads folder
    1. The popup will close
    1. Move the downloaded key file `yourname-key.pem` into a suitable directory
        1. **DO NOT** put this in any Git folder - this would be like adding a password to git, but worse, which is **VERY BAD**
    1. The name should autofill in the `Key pair` section
1. In the `Network Settings` section,
    1. Click the `Edit` button on the right hand side
    1. Change the `VPC` to `RedshiftVPC`
    1. And use the Subnet dropdown to change it to the `RedshiftPublicSubnet0` subnet
    1. Under `Auto-assign Public IP`, select `Enable`
    1. Under `Firewall(security group)`, select `Existing security group`
    1. Under `Firewall(security group)`, use the Security groups dropdown to select the security group, you created earlier (e.g `your-name-sg`)
1. In the `Configure storage` section,
    1. Click the `Advanced` link on the top right
    1. Click the drop-down arrow next to `Volume 1`
    1. Under `Encrypted` select `Encrypted` from the dropdown
    1. Leave everything else as is!
1. In the `Advanced details` section,
    1. Change the `IAM Instance profile` to `de-academy-ec2-role-instance-profile`
    1. Do not touch any other settings here
1. Click on the orange button on the right hand side, to `Launch instance`
1. Navigate to `Instances` and select the `Instance ID` value of your instance
1. Wait for your instance to have an instance state of `Running` before moving on
    1. This should only take about 30 seconds

### Accessing the Instance

Your instance has now been spun up and is ready to be accessed. Let's see how we can go about getting inside it:

1. On your instance summary page, select `Connect` in the top-right of the webpage
1. Select the `SSH Client` tab and copy the long `ssh` command under `Example:`

Now follow the below steps on your terminal (use `wsl` if on Windows):

1. Open a terminal in the folder your downloaded key file is in e.g. `yourname-key.pem`
1. Run: `chmod 400 {name-of-key}.pem`
1. Paste the `ssh` command you copied and hit enter
1. You will be asked `Are you sure you want to continue connecting (yes/no/[fingerprint])?`, type `yes` and hit enter
1. You should now be logged in!
    1. Your terminal prompt should change to show you are inside the instance!

### Setting up the website

1. Elevate your privileges by running: `sudo su`
1. Update all of the packages on the instance: `yum update -y`
1. Install an apache webserver: `yum install httpd -y`
1. Change directory to /var/www/html with `cd /var/www/html`
1. Run `nano index.html`, copy/paste the contents of the `index.html` handout and save the file
    1. To copy the contents you need to open the `index.html` file with a text editor to get the html from it
1. Start the webserver: `service httpd start`
1. Configure the web server to restart if it gets stopped: `chkconfig on`
1. Copy the IP address of your instance, you can find it under `Public IPv4 address` on the instance page in AWS.
1. Paste the address into your browser and watch the magic happen... Hope you like it 😉

**Note**: If you can't browse to it and you are using Chrome (or similar), it will try to default to `https:xxx`. This won't work, so change the URL to `http:xxx` instead.

### Extending our security

The problem with our current setup is that we're relying on having a key file on our machine. Think about the below:

- What if we lose the key?
- What if the key is leaked online?
- What if someone at a company leaves, how do we safely transfer the key?
- What if multiple people want to access the EC2 instance, how would they safely distribute the key?

Is there a way we can login to our instance without needing to worry about keys? We can with a tool called `SSM Agent`.

`SSM Agent` is Amazon software that can be installed and configured on an EC2 instance. This will remove the need for us to use a key to access our instance. This works by configuring and ensuring the correct people are accessing it with IAM policies and roles. It also means we can close off port 22 inbound access so we increase security even further.

After setting up our EC2 instance so it has the correct permissions to communicate with SSM, we could access our instance without SSH or a .pem key as follows:

1. Copy your EC2 instance ID
1. Run the command `aws ssm start-session --target [instance_id] --profile [name_of_profile] --region eu-west-1`

Using SSM lets AWS do all the legwork for applying security restrictions as opposed to putting that on the user. We won't go over manually configuring SSM in this session, but this approach would be preferred over direct SSH access on a real world project.

### Wrapping up

When you are done with this part of the exercise, please delete the following:

1. Any EC2 instances you created
1. Any security groups you created
1. The `.pem` file you downloaded

---

## AWS S3

S3 has a wide range of features, it isn't _just_ for storing objects.

### Part - 1 Dealing with files

Use the AWS CLI in your terminal to perform the following actions. You will need to look up the commands (see below). if you get stuck, sample commands to use are in the `aws/solutions` folder.

1. Log in with `aws sso login --profile <your-profile-name>` or `aws-azure-login --profile <you-profile-name>` depending on your AWS login method
1. Using the CLI, create two S3 buckets (bucket names are **globally** unique, so if someone in the world already created a bucket called `Test123`, you will not be able to use it)
1. Upload a handful of files of your choosing to the first one (make sure there is no personal information in them)
    1. You could use the files in the `handouts` folder, for example
1. _List_ your buckets
1. _List_ the files in your first bucket
1. _Copy_ a file from the first to second bucket
1. _Move_ a file from the first to second bucket
1. _Delete_ a file from either bucket

NB: Make sure to put `--profile your-profile-name` at the end of every command to specify your personal profile.

Hint: Here is a link to the [S3 CLI docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html) - us these to work out the commands you need.

### Part 2 - Setup a website in S3

In this exercise we will be leveraging S3 in a slightly more unusual way. S3 is a fantastic tool for hosting static websites. On a static website, individual webpages include static content. They might also contain client-side scripts.

A lot of websites are becoming static websites which means they run zero server side code and consist of only HTML, CSS and JavaScript. With no server side code to run, there is no reason to host them on a traditional server.

By using the static website hosting feature on an S3 bucket, we can host static websites for one to two dollars a month and scale to handle millions of users. So let's try it out!

#### Setting up the bucket

1. Navigate to the S3 console and click `Create bucket`
1. Enter a name for the bucket (bucket names are globally unique, so if someone has taken your name, tough!)
1. Set the `AWS Region` to `eu-west-1`
1. Scroll to the bottom and hit `Create bucket` again
1. Open up the created bucket
1. Navigate to `Permissions --> Block public access (bucket settings) --> Edit`
1. Ensure all checkboxes next to and below `Block all public access` are ticked (they should be by default)
1. Now we need to upload `index.html` to our bucket. This file will have been provided to you. On the `Objects` tab of your bucket, select `Upload`
1. Drag and drop the file onto the screen to upload it

#### Setting up a CloudFront distribution

CloudFront is AWS's content delivery network (CDN) that caches and delivers web content from edge locations worldwide, reducing latency and improving load times for users. It optimises content delivery by serving cached copies of your website's assets from the nearest edge location to users, ensuring fast and reliable performance.

Because we have securely set up our bucket to block public access, we need to configure a CloudFront distribution so we can access bucket contents via HTTPS.

1. Navigate to the CloudFront service homepage in the AWS Console
1. Click the `Create Distribution` button
1. Under `Origin domain` select the `<bucket-name>.s3.amazonaws.com` URL for the bucket you just created and enter a name for it under `Name`
1. Under `Origin access` select `Legacy access identites`, click the `Create new OAI` button, and enter a name for it.
1. Ensure you select your newly created OAI under `Origin access`
1. Under `Bucket policy` select `Yes, update the bucket policy`
1. Under `Default cache behavior`, select:
    1. Viewer protocol policy -> HTTPS only
    1. Cache key and origin requests -> Legacy cache settings
    1. Leave everything else the same
1. Under `WAF` select `Do not enable security protections`
1. Under `Settings > Supported HTTP versions` also tick `HTTP/3`
1. Under `Default root object`, enter `index.html`
1. Finally, enter a description at the bottom, and click `Create distribution`

Once your CloudFront distribution changes out of `Deploying` state, it's ready!

Everything should be set up at this point, so navigate to the `General` tab of the distribution you made, and copy the `Distribution domain name` URL. Open the URL in a new browser window and voila.. your index.html file should be getting served and cached over HTTPS!

---

## AWS Lambda

### Setup

1. Navigate to `Lambda` on AWS
1. Create a new function and select `Author from scratch`
1. Give your function a unique name and select `Python 3.8` as the runtime and create the function
1. Expand `Change default execution role`
    1. Select `Use an existing role`
    1. Select `lambda-execution-role`
1. Expand Advanced Settings
    1. Select `Enable VPC`
    1. Select `RedshiftVPC` (this is very small text in the box!)
    1. Select `RedshiftPrivateSubnet0`
    1. Select `default VPC security group`
1. Select `Create function`. You will be directed to your new lambda

### Executing some code

1. Navigate to the `Code source` window on the page. Double-click on the `lambda_function.py` file to open the file for editing.
1. Insert the below code and update the string to include your name. Watch out for formatting when you paste it.
1. Click the deploy button.

```py
import json

def lambda_handler(event, context):
    return {
        'body': json.dumps('Hello [insert name]!')
    }
```

1. Click the `Test` button, this will display a pop-up. Select the `hello-world` template and give the event a name. Click `Save`
1. Click `Test` again to run the lambda, you should see a response with your name in the result window below!

```sh
{
    "body": "\"Hello [insert name]!\""
}
```

### Interacting with other AWS services

We've managed to create a basic lambda function. Let's try something more exciting to show the capabilities of lambda. We'll update the code we just deployed. We will use the lambda to upload a file we've created locally to the S3 bucket you created earlier.

1. Go back to your lambda and paste in the code below
1. Update the bucket name to one you've created (make a new one if you need to)
1. Deploy the lambda and test it
1. Navigate back to your S3 bucket, you should now see a file called `hello.txt` in there!

```py
import json
import boto3 # library used to access AWS API
import os

def lambda_handler(event, context):
    os.chdir('/tmp')
    bucket = 'your-bucket-name-here'
    filename = 'hello.txt'
    client = boto3.client('s3')

    response = client.put_object(
        Body="Hello your-name!",
        Bucket=bucket,
        Key=filename
    )
```

What happened? We created a lambda with basic permissions. The permissions applied came bundled with the role we applied to it. You can view the policy attached to the role to get an idea of what is happening. The policy has an action of `s3:PutObject` which means the lambda has permission to call the `PutObject` operation for `S3`. This allows the lambda to upload objects to an S3 bucket. The policy is very broad as it allows the lambda to put an object into _any_ bucket in our account. We would normally restrict access to a specific bucket, or set of buckets. For this exercise though, it won't be a problem.

If we removed that permission, we would get an error when the lambda attempts to put the object when calling the AWS API via `boto3`.

As lambdas are essentially containers under the hood (think back to Docker), it comes with an underlying file system where we can perform operations such as `os.chdir('/tmp')`. The `tmp` folder allows us to create temporary files and hold them before the lambda terminates. Once terminated, the file(s) will be lost.

We created an AWS client with the `boto3` library, which can be used for virtually any AWS service. In our case, we used S3. The S3 API contains a multitude of functions that can be called to interact with S3.

### Wrapping Up

- Delete any Lambda(s) you created for this session.
- Delete all object(s) inside all the S3 bucket(s) you created, then delete all your bucket(s).
