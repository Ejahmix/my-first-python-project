# strings.py
# String operations through the lens of AWS EC2 resource management

instance_id = "i-0abcd1234efgh5678"
status = "  running  "
arn = "arn:aws:s3:::my-company-backups"
log_entry = "ERROR: Instance i-0abc failed health check at 14:32:07"
region = "us-east-1"
instance_type = "T2.MICRO"

# --- Basics ---
print(len(instance_id))         #how many characters
print(instance_id.upper())      # all caps
print(instance_id.lower())      # all lowercase
print(status.strip())          # remove whitespace


# --- Searching ---
print(instance_id.startswith("i-"))  # check if instance_id starts with "i-"
print(arn.startswith("arn:aws:s3"))  # check if arn starts with "arn:aws:s3"
print("Error" in log_entry)          # check if "Error" is in log_entry
print(log_entry.count("i-0abc"))     # count occurrences of "i-0abc" in log_entry

# --- Slicing ---
print(instance_id[0:2]) # "i-" — characters 0 and 1
print(instance_id[2:]) # everything ater "i-"
print(arn.split(":")) # split arn into parts by ":"
print(log_entry.split(" ")[0]) # First word only "ERROR"

# --- Replacing ---
print(status.strip().replace("running", "stopped" ))
print(region.replace("us-east-1", "us-west-2"))

# --- f-strings with formatting ---
cost = 142.5678
print(f"Monthly cost: ${cost:.2f}") # format cost to 2 decimal places
print(f"Instance: {instance_id:>30}") # right-align instance_id in a 30-character field
print(f"Region: {region.upper()}") # method call inside f-string )

print(arn.split(":")[-1])
print(log_entry.split(" ")[1])
print(instance_id[-4:])