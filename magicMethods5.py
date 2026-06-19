import os
import shutil
import uuid

class TempDir:
    def __init__(self):
        # Generate a unique directory name using UUID4
        self.dir_name = f"temp_{uuid.uuid4().hex}"
        self.saved_cwd = None

    def __enter__(self):
        # 1. Save the current working directory path
        self.saved_cwd = os.getcwd()

        # 2. Create the unique temporary directory
        os.mkdir(self.dir_name)

        # 3. Change the current working directory to the new temporary one
        os.chdir(self.dir_name)

        # Return the absolute path of the new directory (optional, but standard practice)
        return os.getcwd()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 1. Restore the previous working directory first
        # (Must move out of the directory before we can safely delete it)
        if self.saved_cwd:
            os.chdir(self.saved_cwd)

        # 2. Clean up and completely remove the temporary directory and all files inside it
        if os.path.exists(self.dir_name):
            shutil.rmtree(self.dir_name)

        # Return False to propagate any exceptions that occurred inside the block
        return False


if __name__ == "__main__":
    # Record our original starting directory path
    original_directory = os.getcwd()
    print(f"Starting directory: {original_directory}")
    with TempDir() as temp_path:
        print(f"Entered context. Active directory: {os.getcwd()}")

        # Assertion 1: Verify the active directory has changed to the unique name
        assert os.getcwd() != original_directory
        assert os.path.basename(os.getcwd()).startswith("temp_")

        # Create a dummy file to verify everything gets cleaned up later
        with open("test_file.txt", "w") as f:
            f.write("This file lives in the temporary directory scope.")

        # Assertion 2: Verify the file exists right now
        assert os.path.exists("test_file.txt")
        print("Successfully created 'test_file.txt' inside the temporary scope.")

    # --- After exiting the context manager ---
    print(f"Exited context. Active directory: {os.getcwd()}")

    # Assertion 3: Verify we are safely back in our starting directory
    assert os.getcwd() == original_directory
    # Assertion 4: Verify the unique directory and its file are completely gone
    assert not os.path.exists(temp_path)

    print("All TempDir context manager assertions passed successfully!")