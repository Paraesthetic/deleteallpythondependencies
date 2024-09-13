import pkg_resources
import subprocess
import sys

def main():
    # Packages to exclude from uninstallation
    exclude_packages = {'pip', 'setuptools', 'wheel'}

    # Retrieve a list of all installed packages
    installed_packages = [dist.project_name for dist in pkg_resources.working_set 
                          if dist.project_name not in exclude_packages]
    
    # Display the list of installed packages
    print("The following packages are installed:")
    for package in installed_packages:
        print(f"- {package}")

    # Confirm uninstallation
    confirm = input("\nAre you sure you want to uninstall all these packages? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Operation cancelled.")
        sys.exit()

    # Uninstall each package
    for package in installed_packages:
        print(f"Uninstalling {package}...")
        subprocess.call([sys.executable, '-m', 'pip', 'uninstall', '-y', package])

    print("\nAll specified packages have been uninstalled.")

if __name__ == '__main__':
    main()
