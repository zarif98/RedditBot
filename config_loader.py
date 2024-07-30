import os
import json
from dotenv import load_dotenv

def load_configuration():
    # Load .env file
    load_dotenv()
    
    # Read JSON file
    json_path = os.path.join(os.path.dirname(__file__), 'search.json')
    with open(json_path, 'r') as json_file:
        json_config = json.load(json_file)
    
    # Combine configurations
    config = {
        **json_config,
        **{k: v for k, v in os.environ.items() if k in [
            'PUSHOVER_APP_TOKEN', 'PUSHOVER_USER_KEY', 'REDDIT_CLIENT_ID',
            'REDDIT_CLIENT_SECRET', 'REDDIT_USER_AGENT', 'REDDIT_USERNAME',
            'REDDIT_PASSWORD'
        ]}
    }
    
    return config