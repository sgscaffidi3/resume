import getpass
from env_manager import GeminiEnvManager

# --- VERSIONING ---
VERSION_MAJOR = 0
VERSION_MINOR = 1 # MANUAL UPDATE: Minor version incremented for Release 0.3.7
CHANGELOG = [
    "Starting at 0.1, after re-initializing log."
]
# --- END VERSIONING ---

def run_setup_flow():
    """Handles the user interaction to ensure a valid API key is available."""
    print("--- Application Setup ---")
    
    key_manager = GeminiEnvManager()
    print(f"Using environment file located at: {key_manager.env_path.absolute()}")
    print("-" * 30)

    current_key = key_manager.get_key()

    if not current_key:
        print("\n[Status] No API Key found in configuration.")
    else:
        masked_key = f"{current_key[:4]}...{current_key[-4:]}" if len(current_key) > 10 else "Invalid/Short"
        print(f"\n[Status] Current Key configured: {masked_key}")

    print("\nChecking connectivity with Google AI...")
    is_valid, message = key_manager.test_key_validity()

    if is_valid:
        print(f"[Success] {message}")
        print("\n--- Configuration Complete ---")
        return current_key

    print(f"[Failure] {message}")
    print("\nYou need to provide a valid Google Gemini API Key.")
    print("Get one here: https://aistudio.google.com/app/apikey")
    
    while True:
        new_key_input = getpass.getpass(prompt="\nEnter your GEMINI_API_KEY (input hidden): ")
        
        if not new_key_input.strip():
             print("Key cannot be empty. Try again.")
             continue

        print("\nUpdating configuration...")
        success_update, update_msg = key_manager.update_key(new_key_input)
        print(update_msg)

        if success_update:
             print("Verifying new key...")
             is_valid_new, message_new = key_manager.test_key_validity()
             if is_valid_new:
                  print(f"[Success] {message_new}")
                  print("\n--- Configuration Complete ---")
                  return new_key_input
             else:
                  print(f"[Failure] The new key did not work: {message_new}. Please try again.")
        else:
             print("Could not save the key locally. Please check file permissions.")
             return None 

if __name__ == '__main__':
    run_setup_flow()