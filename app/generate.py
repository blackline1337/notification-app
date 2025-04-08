# this script will generate a unique api path and api key to be used with the app
# the token and api path are to be used to add messages to the application db, messeges will be deleted in the time frame selected
import secrets
import configparser
import os
from datetime import datetime


def generate_new_keys():
    """Generate new API key and path"""
    return {
        'api_key': secrets.token_hex(32),
        'api_path': secrets.token_hex(16)
    }

def create_default_config(keys):
    """Create a new config with provided keys"""
    config = configparser.ConfigParser()
    config['secrets'] = keys
    return config

def update_config(config, section, key, value):
    """Update a specific configuration value"""
    if not config.has_section(section):
        config.add_section(section)
    config[section][key] = value

def save_config(config, filename='secretkeys.conf'):
    """Save the configuration to a file"""
    with open(filename, 'w') as configfile:
        config.write(configfile)

def generate_config():
    """Main function to generate and save configuration"""
    keys = generate_new_keys()
    
    # Create or load existing configuration
    config = configparser.ConfigParser()
    if os.path.exists('secretkeys.conf'):
        config.read('secretkeys.conf')
        # Update existing config with new values
        update_config(config, 'secrets', 'api_key', keys['api_key'])
        update_config(config, 'secrets', 'api_path', keys['api_path'])
    else:
        # Create new config with default values
        config = create_default_config(keys)
    
    # Save the configuration
    save_config(config)
    return keys

def main():
    keys = generate_config()
    print("Configuration file has been created/updated successfully!")
    print(f"API Key: {keys['api_key']}")
    print(f"API Path: {keys['api_path']}")
    print(f"Api URL: http://localhost:8000/{keys['api_path']}")

if __name__ == "__main__":
    main()