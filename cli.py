import argparse
import sys
# Import all modules to access their public versioning fields and functions
import env_manager
import app_setup
import resume_generator

# --- VERSIONING FOR MAIN APP ---
APP_VERSION_MAJOR = 0
APP_CHANGELOG = [
    "Created main command-line interface script.",
    "Implemented the complex version calculation and --version command.",
    "Integrated run_app_flow to execute the main resume generation logic.",
    "**RELEASE 0.3.X PREP:** Consolidated all prior changelogs into release notes and updated MINOR version across all modules."
]
# --- END VERSIONING ---

def calculate_app_version():
    """Calculates the MAJOR.MINOR.PATCH version of the main application."""
    
    # 1. Determine Minor Version (Sum of all imported minors)
    minor_version = (
        env_manager.VERSION_MINOR +
        app_setup.VERSION_MINOR +
        resume_generator.VERSION_MINOR
    )
    
    # 2. Determine Patch Version (Sum of all changelog lengths)
    patch_version = (
        len(APP_CHANGELOG) +          # Patches for cli.py itself
        len(env_manager.CHANGELOG) +  # Patches for env_manager.py
        len(app_setup.CHANGELOG) +    # Patches for app_setup.py
        len(resume_generator.CHANGELOG) # Patches for resume_generator.py
    )

    return f"{APP_VERSION_MAJOR}.{minor_version}.{patch_version}"

def display_version(current_app_version):
    """Displays the version information for the application and its components."""
    
    print("\n--- Project Version Information ---")
    print(f"Application (cli.py) Version: {current_app_version}")
    
    # Helper function to format module version
    def get_module_version(module):
        major = getattr(module, 'VERSION_MAJOR', 0)
        minor = getattr(module, 'VERSION_MINOR', 0)
        patch = len(getattr(module, 'CHANGELOG', []))
        return f"{major}.{minor}.{patch}"

    print("\nComponent Versions:")
    print(f"  - env_manager.py:      {get_module_version(env_manager)}")
    print(f"  - app_setup.py:        {get_module_version(app_setup)}")
    print(f"  - resume_generator.py: {get_module_version(resume_generator)}")
    
    print("\n--- Changelog Summary ---")
    print("cli.py Changes:")
    for i, entry in enumerate(APP_CHANGELOG, 1):
        print(f"  {i}. {entry}")
    print("\nenv_manager.py Changes:")
    for i, entry in enumerate(env_manager.CHANGELOG, 1):
        print(f"  {i}. {entry}")
    print("\napp_setup.py Changes:")
    for i, entry in enumerate(app_setup.CHANGELOG, 1):
        print(f"  {i}. {entry}")
    print("\nresume_generator.py Changes:")
    for i, entry in enumerate(resume_generator.CHANGELOG, 1):
        print(f"  {i}. {entry}")
    print("-" * 35)

def run_app_flow():
    """Runs the full resume generation process."""
    
    from resume_generator import RESUME_TEXT, USER_ANSWERS 

    # 1. Run the setup flow to get the validated key
    validated_api_key = app_setup.run_setup_flow()

    if validated_api_key:
        # 2. Run the core generation logic
        html_output = resume_generator.generate_seven_resumes_html(validated_api_key, RESUME_TEXT, USER_ANSWERS)

        if html_output:
            output_filename = "tailored_resumes_output.html"
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(html_output)
            
            print(f"\n✅ SUCCESS!")
            print(f"The HTML document containing all 7 resumes has been saved to: {output_filename}")
            print("Open this file in your browser, copy sections, and paste into Word.")
    else:
        print("\nFATAL: Resume generation aborted due to missing or invalid API Key.")
        sys.exit(1)


if __name__ == '__main__':
    app_version = calculate_app_version()
    
    parser = argparse.ArgumentParser(description="Tailored Resume Generator CLI.")
    
    parser.add_argument(
        '--version', 
        action='store_true', 
        help='Display version information for the application and its components.'
    )
    
    args = parser.parse_args()

    if args.version:
        display_version(app_version)
    else:
        run_app_flow()