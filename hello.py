# hello_cloud.py
# My first Python script — simulates what a cloud inventory tool does

# --- Variables and data types ---
engineer_name = "Your Name"        # string
years_experience = 0               # integer
is_certified = False               # boolean
cloud_platforms = ["AWS", "GCP", "Azure"]  # list
aws_services = {                   # dictionary
    "compute": "EC2",
    "storage": "S3",
    "serverless": "Lambda"
}

# --- Print a welcome message ---
print(f"Engineer: {engineer_name}")
print(f"Certified: {is_certified}")
print(f"Platforms: {cloud_platforms}")

# --- Loop through a list ---
print("\nCloud platforms I'm learning:")
for platform in cloud_platforms:
    print(f"  - {platform}")

# --- Loop through a dictionary ---
print("\nAWS services:")
for category, service in aws_services.items():
    print(f"  {category}: {service}")

# --- Simple conditional ---
if is_certified:
    print("\nStatus: certified cloud engineer")
else:
    print("\nStatus: in training — watch this space")