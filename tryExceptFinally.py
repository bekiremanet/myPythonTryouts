try:
    x = float("1245")
    print("I'm here.")

except ValueError:
    print("MISTAKE")

finally:
    print("Application is over.This is always run.")
