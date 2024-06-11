import re
from collections import Counter

def analyze_log(log_file):
    # Regular expressions to match common log patterns
    ip_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    status_code_regex = r' \d{3} '
    requested_page_regex = r'\"(GET|POST|PUT|DELETE) ([^\s]+)'

    # Initialize counters
    status_code_counter = Counter()
    requested_page_counter = Counter()
    ip_counter = Counter()

    with open(log_file, 'r') as file:
        for line in file:
            # Extract information from each log line using regular expressions
            ip = re.search(ip_regex, line).group()
            status_code = re.search(status_code_regex, line).group().strip()
            requested_page = re.search(requested_page_regex, line).group(2)

            # Update counters
            status_code_counter[status_code] += 1
            requested_page_counter[requested_page] += 1
            ip_counter[ip] += 1

    # Print summarized report
    print("Number of 404 errors:", status_code_counter['404'])
    print("Most requested pages:")
    for page, count in requested_page_counter.most_common(5):
        print(f"{page}: {count} requests")
    print("IP addresses with the most requests:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} requests")

if __name__ == "__main__":
    log_file = "sample.log"  # Path to your web server log file
    analyze_log(log_file)
