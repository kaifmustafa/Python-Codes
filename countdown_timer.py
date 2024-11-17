import time

def countdown_timer():
    try:
        time_in_seconds = int(input("Enter time in seconds for countdown: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    
    while time_in_seconds:
        mins, secs = divmod(time_in_seconds, 60)
        time_format = f"{mins:02}:{secs:02}"
        print(time_format, end='\r')
        time.sleep(1)
        time_in_seconds -= 1

    print("Time's up!")

# Run the timer
if __name__ == "__main__":
    countdown_timer()