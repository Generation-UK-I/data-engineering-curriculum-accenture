# Monitoring Exercises

## Cloud Logging

You will create a cloud function which will generate logs that we can query. Once uploaded and ran, it will generate 100 logs.

1. Head to the [Cloud functions](https://console.cloud.google.com/functions).
Click `Create function` input a name in `Function name` field, leave rest as is.
1. Now click next which opens up the code window , select the Runtime to python 3.9
1. Copy the code from `main.py` and paste into the inline editor
1. Update the entry point to be `log_demo`
1. Now click `Deploy` button at the bottom left screen.

### Test the function

1. *if created via CLI navigate to your cloud functions* Select your newly created
1. Go to the `TESTING` tab and click `TEST THE FUNCTION`.
1. It will take few moments for some logs to start showing in the screen.
1. Go to [Log Explorer](https://console.cloud.google.com/logs/query) here you can query for the logs you want to see.

For context, this Lambda establishes a new logger and loops 100 times.
Within this loop, it calculates two properties that we can see in the logs. `statusCode` is randomly chosen each time as success (`200`) or failure (`500`).
Elapsed time is calculated by randomly selecting a number between 0 and 1 and then sleeps for that duration in seconds. The logged time is the total time the lambda ran. Both properties are logged in the form of JSON. You can see the two properties bundled up in the `message` property.

### Query the logs

1. In the Query text field enter the below
1. Search for resource type using `resource.type="cloud_function"`
1. Search for the function name using `resource.labels.function_name="{function-name}"`
1. Click the `Run Query` button on the top right
1. You can use the severity dropdown above the text box to select `ERROR` or `INFO` to see only the error or info logs.
1. Try the below and see what they do:

```sh
resource.type="cloud_function"
resource.labels.function_name="<your-function-name>"
jsonPayload.message.statusCode = 500
jsonPayload.message.executionTime > 0.5
```

The json object we printed in our code is picked up and parsed by Cloud Logging and is placed into `jsonPayload` and also severity is detected.

You can use logging libraries too. For more information see [Writing Structured log](https://cloud.google.com/functions/docs/monitoring/logging#writing_structured_logs)

You can find more information about the syntax [here](https://cloud.google.com/logging/docs/view/logs-viewer-interface).

---

## Cloud Monitoring

Using GCP monitoring console, create a dashboard with this naming format `temp-2022-jlr-de-<your-name>` that shows some metrics about your recently created cloud function and also some metrics about your Bigquery datasets.

---

## Grafana

This exercise will get you to start up an instance of Grafana. You will set up two data sources and display them in a dashboard on different panels.

### Setting up Grafana

1. Ensure Docker is running on your machine.
1. To both pull down the Grafana image and start the container, run the following command:

    ```sh
    docker run -d -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=grafana-simple-json-datasource" grafana/grafana
    ```

1. Confirm that you can see the dashboard by opening `localhost:3000` on your browser
1. You can login with the default credentials. Both username and password are `admin`. It will ask you to choose a new password, input whatever you want here

### Data source setup

Open a terminal in the `handouts` folder.

Run `pip install flask` to make sure you have it.

Run the `handouts/grafana_data.py` file that was supplied to you as part of this exercise.

- This will run a service on port `5000` and will generate some random data for us to display in Grafana

Once you have logged into the Grafana dashboard, you can tell Grafana where to look for data. We will be using a combination of the random data generated from `grafana_data.py`, as well as a test database that comes with Grafana.

1. On the left hand side, hover your mouse over the configuration icon and select `Data Sources`
1. Select `Add data source`
1. Scroll down to the very bottom and select `Find more data source plugins` and put "JSON" in the search box
1. Select `SimpleJson` from the list
1. In the `URl` textbox, set it to <http://host.docker.internal:5000>
1. Enter a name and then select `Save & Test`
1. Check the Green OK message is created and then press the `Back` button
1. Again, select `Add data source`
1. Select "TestData DB" from the list, then enter a name and then select `Save & Test`
1. Check the Green OK message is created and then press the `Back` button

### Setting up a dashboard

Now that we have the relevant data sources, we can hook them up to some visualisations for a dashboard we will put together.

1. Hover over the `+` icon on the left and select `Dashboard`.
1. Press the `Add New Panel` button. You will see a random looking graph and a bunch of other configuration.
1. Under the `Query` tab under the graph, select `TestData DB` from the dropdown.
1. Select `Random Walk` from the `Scenario` dropdown.
1. Select the `Apply` button in the top right corner. This will take us to our new dashboard with a generated graph.
1. Select the `Add panel` button in the top right and then the `Add new panel` button.
1. Under the `Query` tab under the graph, select `SimpleJson` from the dropdown.
1. Select `my_series` from the `select metric` dropdown.
1. Select the `Apply` button in the top right corner. This will take us back to our dashboard with another generated graph.
1. The dashboard should now have two panels.

### Changing our data

1. Select the dropdown next to the refresh button in the top right corner. Set the option to "5s" or "10s" to set the auto refresh time.
1. In `grafana_data.py`, comment the current data points and un-comment the new data points. Watch what happens to the displayed data. It will have tilted the line.
1. Stop the python app and see what happens to the panel. It will automagically tell us that there is no data to display.

### Changing our panels

There are plenty of ways of displaying data in Grafana. How do we change how our data is being displayed?

1. Press the arrow by the `Panel Title` to bring up the menu and select `Edit`
1. In the `Scenario` dropdown, select a few different scenarios and see the change in the panel data. Lots of cool looking visuals going on!
