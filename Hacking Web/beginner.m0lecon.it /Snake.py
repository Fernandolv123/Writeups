import requests
import json

def submit_score(score, player_name):
    url = "https://snake1.challs.m0lecon.it/api/submit-score"
    
    data = {
        "score": score,
        "playerName": player_name
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.post(
        url, 
        json=data, 
        headers=headers,
        timeout=10
    )
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(json.dumps(result, indent=2))
    else:
        print(response.text)

if __name__ == "__main__":
    print("START")
    submit_score(1500, "Miku")
