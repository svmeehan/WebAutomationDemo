import json

def lambda_handler(event, context):
    inputCurrency = event['inputCurrency']
    outputCurrency = event['outputCurrency'] 
    inputAmount = event['inputAmount'] 

    outputAmount = inputAmount * 0.5
    # TODO implement
    return {
        'statusCode': 200,
        'outputAmount': outputAmount,
        'outputCurrency': outputCurrency
    }
