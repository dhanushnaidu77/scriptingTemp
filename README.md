Server Health Check Script

This Python script monitors the health of endpoints listed in a CSV file. It sends an email notification if an endpoint is down or returns a non-200 status code. The script reads endpoint URLs from a CSV file, checks their availability, and sends alerts via Gmail if any issues are detected.

Key features:

Reads endpoint URLs from a CSV file.
Sends a detailed email notification if an endpoint is down.
Includes error handling for network and email sending failures.
