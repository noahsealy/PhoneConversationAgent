import os

def get_env_value(key):
    # Load the env variables
    load_env()
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                # Skip empty lines and comments
                if line.strip() and not line.startswith('#'):
                    env_key, value = line.strip().split('=', 1)
                    if env_key == key:
                        return value
    return None

def load_env():
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
