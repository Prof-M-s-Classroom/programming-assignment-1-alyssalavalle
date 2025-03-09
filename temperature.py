from datetime import datetime

class Temperature:
    """
    Class to represent a temperature reading with humidity and timestamp.
    """
    def __init__(self, temperature, humidity):
        """Initialize the Temperature object with temperature, humidity, and timestamp."""
        self.temperature = temperature
        self.humidity = humidity
        self.timestamp = datetime.now()

    def __str__(self):
        """Return a formatted string representation of the Temperature object."""
        return f"Temperature: {self.temperature}°C, Humidity: {self.humidity}%, Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
