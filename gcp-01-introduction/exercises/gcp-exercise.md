# GCP Exercises

---

## GCP Account Setup

1. Click [Google cloud console](https://cloud.google.com/)
1. Click on sign in - top right corner of the page
1. Login with your credentials provided
1. use the **password** you were issued or your previously set **password**

1. If multifactor authentication (MFA) is enabled on the account, use that to login for secure access.
1. Click **Accept** to indicate your acknowledgement of Google's terms of service and privacy policy
1. On the **Protect your account** page, click **Confirm**
1. On the **Welcome** page, check **Terms of Service** to agree to Google Cloud's terms of service, and click **Agree
   and continue**.

1. Click on '_Management console_' and you will be successfully signed into the GCP console.

---

## GCP SDK Setup

### Installation

**Windows**:

- Download the [latest version](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe).

Alternatively, open a PowerShell terminal and run the following PowerShell commands:

> (New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
> & $env:Temp\GoogleCloudSDKInstaller.exe

- Launch the installer and follow the prompts. The installer is signed by Google LLC

- After installation is complete, the installer gives you the option to create Start Menu and Desktop shortcuts, start
  Cloud SDK shell, and configure the Cloud SDK

  _Make sure that you leave the options to start the shell and configure your installation selected. The installer
  starts a terminal window and runs the gcloud init command_

- The default installation doesn't include the App Engine extensions required to deploy an application using gcloud
  commands. These components can be installed using
  the [Cloud SDK component manager](https://cloud.google.com/sdk/docs/managing-components).

#### Troubleshooting tips:

- If your installation is unsuccessful due to the find command not being recognized, ensure your PATH environment variable is set to include the folder containing find. Usually, this is C:\WINDOWS\system32;.
- If you have just uninstalled Cloud SDK, you must reboot your system before installing Cloud SDK again.
- If unzipping fails, run the installer as an administrator.

**MacOS**:

- Confirm that you have a supported version of Python

  > Supported versions are Python 3 (3.5 to 3.8, 3.7 recommended) and Python 2 (2.7.9 or higher).
  > Modern versions of macOS include the appropriate version of Python required for the Cloud SDK. To check your current Python version, run python -V.
  > For Cloud SDK release version 352.0.0 and above, the main install script offers to install CPython's Python 3.7 on Intel-based Macs.

- Download one of the following
    - [macOS 64-bit (x86_64)](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-365.0.1-darwin-x86_64.tar.gz)
      4ae8a3274eb9b6fca5761ef2eed713bc3486256d11268575febe3351e9e4d902
    - [macOS 64-bit(arm64, Apple M1 silicon)](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-365.0.1-darwin-arm.tar.gz)
      636591e597730649011f510fc8c78e2b133ef8b417992f8d923a87a528dc6d5e
    - [macOS 32-bit(x86)](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-365.0.1-darwin-x86.tar.gz)
      b3b04f7f5577347d5c30277d4bf6aa2d1a182c1ff8f9cc04edf0dee6f0b8c4a9

- Extract the archive to any location on your file system (preferably your Home directory). On macOS, this can be
  achieved by opening the downloaded .tar.gz archive file in the preferred location
- In the terminal navigate to the extracted folder `google-cloud-sdk` and execute `./install.sh` and follow the inputs

**Initialising the cloud SDK**:

```text
Troubleshooting: You may need to start a new terminal to have the gcloud command available.
```

Use the _gcloud init_ command to perform several common Cloud SDK setup tasks. These include authorizing the Cloud SDK
tools to access Google Cloud using your user account credentials and setting up the default configuration.

To initialise the Cloud SDK:

1. Run the following at a command prompt
   > gcloud init
1. Accept the option to log in using your Google user account
   > To continue, you must log in. Would you like to log in (Y/n)? Y

1. In your browser, log in to your Google user account when prompted and click Allow to grant permission to access
   Google Cloud resources

1. At the command prompt, select a Google Cloud project from the list of those where you have **Owner**, **Editor**
   or **Viewer** permissions

    ```sh
    Pick cloud project to use:
    [1] [my-project-1]
    [2] [my-project-2]
    ...
    Please enter your numeric choice:
    ```

1. _gcloud init_ confirms that you have complete the setup steps successfully

    ```sh
    gcloud has now been configured!
    You can use [gcloud config] to change more gcloud settings.

    Your active configuration is: [default]
    ```

---

## GCE

You're going to setup your own GCE server, then extend it so that we can host a basic website on it. After that we will
look other best practice of using GCE.

### GCE Instance Setup

Now let's Create a virtual machine using the GCP Console.

1. In the `Navigation menu`, click `Compute Engine` > `VM instances`
1. Click `Create an instance`
1. On the `Create an Instance page`, fill out

    - **Name:** my-vm-1
    - **Region:** us-central1
    - **Zone:** us-central1-a
    - **Machine Series:** N1
    - **Machine type:** f1-micro

1. For `Boot disk`, if the Image shown is not `Debian GNU/Linux 10 (Buster)`, click `Change` and
   select `Debian GNU/Linux 10 (Buster)`
1. Leave the defaults for `Identity and API access` unmodified
1. For Firewall, click `Allow HTTP traffic` and `Allow HTTPS traffic`
1. Leave all other defaults unmodified
1. To create and launch the VM, click `Create`
1. Wait for your instance to have an instance state of `Running` before moving on. This should only take about 15-30
   seconds.

### Accessing the Instance and setting up a website

Your instance has now been spun up and is ready to be accessed. Let's see how we can go about getting inside it.

1. To connect to the Linux VM you just created, click `SSH` in the row of the VM
1. You should see screen like below, it is just the bash terminal for Debian 10
1. To update the available packages, run the below command
   > sudo apt update
1. Now we can install Apache, we use the below command
   > sudo apt install apache2

    ```sh
    Hit 'Y' when prompted to continue the installation. This will do everything necessary to install Apache onto your new machine
    ```

   After installing Apache, the operating system automatically starts the Apache server

1. Verify that Apache is running:
   > sudo systemctl status apache2
1. To verify that Apache is running and responding to HTTP requests. Head back to the VM dashboard and click the _
   External IP_ assigned to your VM. This should open a new tab with Apache startup page displayed
1. Overwrite the Apache web server default web page with your personal content

    ```sh
        echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' | sudo tee /var/www/html/index.html
    ```

Hello World! can be updated by updating it in the script above and run the line of code again.

1. To view the updated webpage
   > In a browser, navigate to <http://[EXTERNAL_IP>]

### Wrapping up

When you are done with this part of the exercise, please delete the following:

- Any GCE instances you created.

---

## GCP cloud storage

GCS has a wide range of features, with the flexibility to store structured and unstructured data, it can also be used to
serve static website with a fine-grain access control list (ACL).

### Part - 1 Create a Bucket

Use the GCP cloud console:

1. Go to `Navigation menu` > `Cloud Storage` > `Browser`
1. Click `Create Bucket`
1. Enter your bucket information and click Continue to complete each step

    - **Name your bucket**: Enter a unique name for your bucket - gcs name is global.
    - Choose **Region** for **Location type** and **us-east1 (South Carolina)** for **Location**
    - Choose **Standard** for **default storage class**
    - Choose **Uniform** for **Access control**
    - Choose **None** for **protection tools**
      > These will be useful later in the project
    - Leave the rest info as **default**
1. Click `Create`

    ```sh
    That is it —  you have just created a Cloud Storage bucket!
    ```

### Part 2 - Upload an object and share a Bucket Publicly

1. Right-click on the image above (or any of your favourite
   from [Cat](https://www.google.com/search?q=cat&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjbiZisuL70AhUQZMAKHW9rChAQ_AUoAXoECAIQAw&biw=1920&bih=969&dpr=1))
   and download it to your computer. Save the image as **kitten.jpg**, renaming it on download
1. In the Cloud Storage browser page, click the name of the bucket that you created
1. In the **Objects tab**, click `Upload files`
   > In the file dialog, go to the file that you downloaded and select it
   > Ensure the file is named **kitten.jpg**. If it is not, click the **three dot** icon for your file, select **Rename** from the dropdown, and rename the file to **kitten.jpg**
1. To allow public access to the bucket and create a publicly accessible URL for the image, Click the `Permissions` tab
   above the list of files.
1. Ensure the view is set to **Principals**. Click `Add` to view the **Add principals** pane.
1. In the **New principals** box, enter _allUsers_
1. In the **Select a role** drop-down, select **Cloud Storage** > **Storage Object Viewer**
1. Click `Save`.
1. In the **Are you sure you want to make this resource public?** window, click `Allow public access`.

    ```sh
      To verify, click the Objects tab to return to the list of objects.
      Your object`s Public access column should read Public to internet
    ```

1. The **Copy URL** button provides a shareable URL similar to the following

   > <https://storage.googleapis.com/YOUR_BUCKET_NAME/kitten.jpg>

   **Congratulations!**

---

## GCP Cloud Functions

### Setup

1. Enable relevant APIs

   Click Navigation bar > APIs & Services > Enable APIs & Services

    - Cloud Functions APIs
    - Cloud Build APIs
    - Cloud Storage APIs
    - Eventarc APIs

   > Enabled services Should have a green checked mark with API enabled
1. Go to `Navigation menu` > `Cloud Functions`
1. Click `Create Function`
1. Fill out all information on **create function** page with:

        - Function Name: function-1
        - Region: europe-west2
        - Trigger: HTTP
        - Require authentication: On
        - Requires HTTPS: checked
1. Click `Save` and `Next`
1. Change Runtime to Python3.9
1. Let's analysis the main.py code on the left hand side

        def hello_world(request):
            """Responds to any HTTP request.
            Args:
                request (flask.Request): HTTP request object.
                Returns:
                The response text or any set of values that can be turned into a Response object using
                `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
            """
            request_json = request.get_json()
            if request.args and 'message' in request.args:
                return request.args.get('message')
            elif request_json and 'message' in request_json:
                return request_json['message']
            else:
                return f'Hello World!'

1. Leave everything else as Default
1. Click `DEPLOY`
1. Wait till cloud function is active with green check box before the cloud function you created
1. Click the function you created > navigate to testing tab > Click `test the function`

   > Output: Hello World!

### Interacting with other GCP services

We've managed to create a basic cloud function, Let's try something more exciting to show the capabilities of cloud
function. We'll create a new cloud function which will be triggered when new file is created or file is deleted from the
cloud storage you created earlier.

1. Follow the cloud function steps you performed earlier till step 4. Fill the information below in the page

        - Function Name: function-gcs-create
        - Region: europe-west2
        - Trigger: Cloud storage
        - Event type: Finalize/create
        - Bucket: Browse and select the previously created bucket

1. Click `Save` and `Next`
1. Change Runtime to Python3.9
1. Copy main.py from the handout into cloud function main.py inline editor
1. Leave everything else as Default
1. Click `DEPLOY`
1. Wait till cloud function is active with green check box before the cloud function you created
1. To test your newly built cloud function, upload multiple files into your cloud bucket
   > Under action, click 3 vertical dots and click view logs to see the output from the function you created

### Task

Create a cloud function which triggers when files are deleted from the same cloud storage

> The `main.py` file can be re-used
>
> If versioning is on, the function will not trigger

---

### Wrapping Up

Please tidy up after yourselves:

- Delete any cloud functions you created for this session.
- Delete all objects inside the GCS bucket(s) you created, then delete the bucket(s).
