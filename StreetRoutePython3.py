
import json
import requests
import argparse
import urllib.parse

def main():
  base_service_url = "http://streetroute.melissadata.net/"
  service_endpoint = "v1/WEB/StreetRoute/getDistance"

  # Create an ArgumentParser object
  parser = argparse.ArgumentParser(description='Street Route command line arguments parser')

  # Define the command line arguments
  parser.add_argument('--license', '-l', type=str, help='License key')
  parser.add_argument('--startlat', type=str, help='Starting Latittude')
  parser.add_argument('--startlong', type=str, help='Starting Longitude')
  parser.add_argument('--endlat', type=str, help='Ending Latitude')
  parser.add_argument('--endlong', type=str, help='Ending Longitude')

  # Parse the command line arguments
  args = parser.parse_args()

  # Access the values of the command line arguments
  license = args.license
  starting_lat = args.startlat
  starting_long = args.startlong
  ending_lat = args.endlat
  ending_long = args.endlong

  call_api(base_service_url, service_endpoint, license, starting_lat, starting_long, ending_lat, ending_long)

def get_contents(base_service_url, request_query):
    url = urllib.parse.urljoin(base_service_url, request_query)
    response = requests.get(url)
    obj = json.loads(response.text)
    pretty_response = json.dumps(obj, indent=4)

    print("\n==================================== OUTPUT ====================================\n")

    print("API Call: ")
    for i in range(0, len(url), 70):
        if i + 70 < len(url):
            print(url[i:i+70])
        else:
            print(url[i:len(url)])
    print("\nAPI Response:")
    print(pretty_response)

def call_api(base_service_url, service_endpoint, license, starting_lat, starting_long, ending_lat, ending_long):
    print("\n=================== WELCOME TO MELISSA STREET ROUTE CLOUD API ==================\n")

    should_continue_running = True
    while should_continue_running:
        input_starting_lat = ""
        input_starting_long = ""
        input_ending_lat = ""
        input_ending_long = ""
        if not starting_lat and not starting_long and not ending_lat and not ending_long:
            print("\nFill in each value to see results")
            input_starting_lat = input("Starting Latitude: ")
            input_starting_long = input("Starting Longitude: ")
            input_ending_lat = input("Ending Latitude: ")
            input_ending_long = input("Ending Longitude: ")
        else:
            input_starting_lat = starting_lat
            input_starting_long = starting_long
            input_ending_lat = ending_lat
            input_ending_long = ending_long

        while not input_starting_lat or not input_starting_long or not input_ending_lat or not input_ending_long:
            print("\nFill in each value to see results")
            if not input_starting_lat:
                input_starting_lat = input("\nStarting Latitude: ")
            if not input_starting_long:
                input_starting_long = input("\nStarting Longitude: ")
            if not input_ending_lat:
                input_ending_lat = input("\nEnding Latitude: ")
            if not input_ending_long:
                input_ending_long = input("\nEnding Longitude: ")

        inputs = {
            "format": "json",
            "StartLatitude": input_starting_lat,
            "StartLongitude": input_starting_long,
            "EndLatitude": input_ending_lat,
            "EndLongitude": input_ending_long
        }

        print("\n===================================== INPUTS ===================================\n")
        print(f"\t   Base Service Url: {base_service_url}")
        print(f"\t  Service End Point: {service_endpoint}")
        print(f"\t     Start Latitude: {input_starting_lat}")
        print(f"\t    Start Longitude: {input_starting_long}")
        print(f"\t       End Latitude: {input_ending_lat}")
        print(f"\t      End Longitude: {input_ending_long}")

       # Create Service Call
        # Set the License String in the Request
        rest_request = f"&id={urllib.parse.quote_plus(license)}"

        # Set the Input Parameters
        for k, v in inputs.items():
            rest_request += f"&{k}={urllib.parse.quote_plus(v)}"

        # Build the final REST String Query
        rest_request = service_endpoint + f"?{rest_request}"

        # Submit to the Web Service.
        success = False
        retry_counter = 0

        while not success and retry_counter < 5:
            try: #retry just in case of network failure
                get_contents(base_service_url, rest_request)
                print()
                success = True
            except Exception as ex:
                retry_counter += 1
                print(ex)
                return

        is_valid = False;

        if (starting_lat is not None) and (starting_long is not None) and (ending_lat is not None) and (ending_long is not None):
            concat = starting_lat + starting_long + ending_lat + ending_long
        else:
            concat = None

        if concat is not None and concat != "":
            is_valid = True
            should_continue_running = False

        while not is_valid:
            test_another_response = input("\nTest another record? (Y/N)")
            if test_another_response != '':
                test_another_response = test_another_response.lower()
                if test_another_response == 'y':
                    is_valid = True
                elif test_another_response == 'n':
                    is_valid = True
                    should_continue_running = False
                else:
                    print("Invalid Response, please respond 'Y' or 'N'")

    print("\n===================== THANK YOU FOR USING MELISSA CLOUD API ====================\n")

main()
