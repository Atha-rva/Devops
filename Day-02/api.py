import requests

# API URL 

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    # Send GET Requests 
    response = requests.get(url)

    # Print status code 
    print("Status Code: ", response.status_code)

    # Print Content Type ( should be JSON )
    print("Content Type: ", response.headers.get("content-type"))

    # Print raw text 
    print("Text Reponse: ", response.text)

    # Parse JSON in python dict 

    data = response.json()
    print("JSON Response: ",data)

    print(type(data))

    # for key,value in data.items():
    #     print(key,value)

    # for key,value in data.items():
    #     if key == "completed":
    #         if value == False:
    #             print("The Following Data is not Completed in a Server")


    # for key,value in data.items():
    #     if key == "userId":
    #         if value == [1,2,3,4,5]:
    #             print("The Following Data server is Completed")

    

except requests.exceptions.RequestException as e:
    print("Error Occured:  ",e)