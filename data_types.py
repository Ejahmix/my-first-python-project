# data_types.py
# Explorting python data types through an AWS EC2 instance

# String
instance_id = "i-0abcd1234efgh5678"
instance_type = "t2.micro"
region = "us-east-1"
availability_zone = "us-east-1a"

#integer
cpu_count = 2
port = 443

# Float
cost_per_hour = 0.023
storage_gb = 20

# Boolean
is_running = False
is_encrypted = False

# None
termination_date = None

# Print everything with labels
print("=== EC2 Instance Profile ===")
print(f"ID: {instance_id}")
print(f"Type: {instance_type}")
print(f"Region: {region}")
print(f"Availability Zone: {availability_zone}")
print(f"CPUs: {cpu_count}")
print(f"Port: {port}")
print(f"Cost/hr: ${cost_per_hour:.3f}")
print(f"Storage: {storage_gb:.1f} GB")
print(f"Running: {is_running}")
print(f"Encrypted: {is_encrypted}")
print(f"Termination Date: {termination_date}")

# Check the types
print("\n=== Data Types ===")
print(type(instance_id))
print (type(cpu_count))
print(type(cost_per_hour))
print(type(is_running))
print(type(termination_date))

print(cpu_count + port)
print(cost_per_hour + storage_gb)
print(instance_id + " is in " + region)
print(str(cpu_count) + " CPUs on instance " + instance_id)
