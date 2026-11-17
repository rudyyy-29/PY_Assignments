
import gc

# Check automatic garbage collection
print("Garbage Collection Enabled:", gc.isenabled())

# Display garbage collection thresholds
print("GC Threshold:", gc.get_threshold())

# Display current collection count
print("GC Count:", gc.get_count())

# Disable automatic garbage collection
gc.disable()
print("\nAutomatic Garbage Collection Disabled")

# Create circular references
a = []
b = []
a.append(b)
b.append(a)

# Delete references
del a
del b

print("Circular references created and deleted.")

# Perform manual garbage collection
collected = gc.collect()
print("Objects collected manually:", collected)

# Enable automatic garbage collection again
gc.enable()
print("\nAutomatic Garbage Collection Enabled:", gc.isenabled())

# Display final garbage collection statistics
print("Final GC Count:", gc.get_count())
print("Final GC Threshold:", gc.get_threshold())
