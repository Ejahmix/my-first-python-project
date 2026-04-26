# hello_cloud.py
# My first Python script — cloud engineer profile

# Variables and data types
engineer_name = "Elijah"
years_experience = 0
is_certified = False
aws_region = "us-east-1"
cloud_platforms = ["AWS", "GCP", "Azure"]
aws_services = {
    "compute": "EC2",
    "storage": "S3",
    "serverless": "Lambda",
    "database": "RDS"
}

# Print profile
print(f"Engineer: {engineer_name}")
print(f"Region: {aws_region}")
print(f"Certified: {is_certified}")
print(f"Platforms: {cloud_platforms}")

# Loop through list
print("\nCloud platforms I am learning:")
for platform in cloud_platforms:
    print(f"  - {platform}")

# Loop through dictionary
print("\nAWS services:")
for category, service in aws_services.items():
    print(f"  {category}: {service}")

# Conditional
if is_certified:
    print("\nStatus: certified cloud engineer")
else:
    print("\nStatus: in training — watch this space")
