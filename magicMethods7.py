from contextlib import ContextDecorator
from datetime import datetime
import os

class LogFile(ContextDecorator):
    def __init__(self, log_file_name: str):
        self.log_file_name = log_file_name
        self.start_time = None

    def __enter__(self):
        # Record the exact start timestamp when entering the context
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 1. Calculate execution duration
        end_time = datetime.now()
        execution_time = end_time - self.start_time

        # 2. Extract error information if an exception occurred
        if exc_val is not None:
            error_message = str(exc_val)
        else:
            error_message = "None"

        # 3. Format the log logline string
        # Formats the datetime string to preserve microseconds exactly like your spec sheet
        start_str = self.start_time.strftime("%Y-%m-%d %H:%M:%S.%f")
        log_line = f"Start: {start_str} | Run: {execution_time} | An error occurred: {error_message}\n"

        # 4. Write to log file in append mode ('a')
        with open(self.log_file_name, "a", encoding="utf-8") as fa:
            fa.write(log_line)
        return False


if __name__ == "__main__":
    log_name = "my_trace.log"

    # Ensure a fresh environment for testing
    if os.path.exists(log_name):
        os.remove(log_name)

    # Test Scenario 1: Clean Context Execution (No Errors)
    with LogFile(log_name):
        a = 10 + 20

    # Read log file to verify structural content
    with open(log_name, "r") as f:
        lines = f.readlines()

    assert len(lines) == 1
    assert "Start:" in lines[0]
    assert "Run:" in lines[0]
    assert "An error occurred: None" in lines[0]
    print("Scenario 1 Passed: Successfully tracked a clean execution block.")

    # Test Scenario 2: Context Execution with Exception Handling
    try:
        with LogFile(log_name):
            val = 1 / 0
    except ZeroDivisionError:
        pass

    with open(log_name, "r") as f:
        lines = f.readlines()

    assert len(lines) == 2
    assert "An error occurred: division by zero" in lines[1]
    print("Scenario 2 Passed: Tracked exception message and reraised it cleanly.")

    # Test Scenario 3: Execution as a Function Decorator
    @LogFile(log_name)
    def decorated_function():
        return "Hello World"

    decorated_function()

    with open(log_name, "r") as f:
        lines = f.readlines()

    assert len(lines) == 3
    assert "An error occurred: None" in lines[2]
    print("Scenario 3 Passed: ContextDecorator compatibility validated successfully!")

    if os.path.exists(log_name):
        os.remove(log_name)