# lists.py
# List operations through the lens of AWS resource management

# --- Creating Lists ---
instances = ["i-0abc", "i-0def", "i-0ghi", "i-0jkl"]
regions = ["us-east-1", "us-west-2", "eu-west-1"]
ports = [22, 80, 443, 8080]
mixed = ["i-0abc", 2, True, None] # lists can hold any type

# --- Accessing Items ---
print(instances[0]) # first instance
print(instances[-1]) # last instance
print(instances[1:3]) # slice of instances index 1 and 2
print(instances[:2]) # first two instances
print(instances[2:]) # all instances from index 2 to end

# --- Basic info ----
print(len(instances)) # number of instances
print("i-0abc" in instances) # check if instance is in list
print("i-0xyz" in instances) # check if non-existent instance is in list

# --- Modifying Lists ---
instances.append("i-0mno") # add new instance to end
print(instances)

instances.insert(0, "i-0zzz") # add new instance at index 0
print(instances)

instances.remove("i-0zzz") # remove instance by value
print(instances)

popped = instances.pop() # remove and return last instance
print(f"Removed: {popped}")
print(instances)

# --- Sorting ---
regions.sort() # sort regions alphabetically
print(regions)

ports.sort(reverse=True) # sort ports in descending order
print(ports)

# --- Looping ---
print("\n=== Running Instances ===")
for instance in instances:
    print(f" instance: {instance}")

# --- Loop with index ---
print("\n=== Indexed ===")
for i, instance in enumerate(instances):
    print(f" instance {i}: {instance}")

# --- List Comprehension - the power move ---
high_ports = [port for port in ports if port > 100]
print(f"\nHigh ports: {high_ports}")

upper_regions = [region.upper() for region in regions]
print(f"Regions uppercase: {upper_regions}")

# Challenge 1 — what does this print?
print(instances[1:3])

# Challenge 2 — build a new list using comprehension
# Make a list of only instances that contain "0d" in their ID
filtered = [i for i in instances if "0d" in i]
print(filtered)

# Challenge 3 — combine two lists
all_resources = instances + regions
print(all_resources)
print(len(all_resources))
