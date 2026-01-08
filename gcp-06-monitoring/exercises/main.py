from random import randint, random
from time import sleep, perf_counter
import json

def log_demo(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Create 100 logs
    for _ in range(100):
        # Record runtime
        start_time = perf_counter()
        
        # Pick a random length of time between 1 and 5 seconds
        sleep_time = random()
        sleep(sleep_time)
        
        # Choose success / failure randomly
        success = randint(0, 1)
        status_code = 200 if success else 500
            
        json_log = {
            'statusCode': status_code,
            'executionTime': perf_counter() - start_time
        }
        
        if success:
            print(
                json.dumps(
                    {
                        "severity": "INFO",
                        "message": json_log
                    }
                ))
        else:
            print(
                json.dumps(
                    {
                        "severity": "ERROR",
                        "message": json_log
                    }
                ))
    return ('logging done!', 200)
