import json

def modify_tokens():
    # Load the file
    with open('telosevm.tokenlist.json', 'r') as file:
        data = json.load(file)

    # Check each token
    for token in data['tokens']:
        # Check if the issuer field is present and has the value 'Multichain'
        if 'issuer' in token and token['issuer'] == 'Multichain':
            # Modify the token
            token['coingeckoId'] = False
            token['cmcId'] = False

    # Write the modified data back to the file
    with open('telosevm.tokenlist.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    modify_tokens()
