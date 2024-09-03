import requests

def lambda_handler(event, context):

    # testing flipkart api
    url = 'https://real-time-flipkart-api.p.rapidapi.com/product-search'
    querystring = {
        "q": "new balance 2002",
        "page": "1",
        "sort_by": "popularity"
    }

    headers = {
        'x-rapidapi-host': 'real-time-flipkart-api.p.rapidapi.com',
        'x-rapidapi-key': '5474778fb9msh8b56259111e5167p1293bejsn5fa61ff373d1'
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'statusCode': 200,
                'body': data
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': f"Failed to fetch data. Status code: {response.status_code}"
            } 
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': f"An error occurred: {e}"
        }

def main():
    with open('test_event.json') as f:
        event = f.read()
    result = lambda_handler(eval(event), None)
    print(result)

if __name__ == "__main__":
    main()
  