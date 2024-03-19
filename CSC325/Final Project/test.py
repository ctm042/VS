from collections import namedtuple

class BloomFilter:
  """
  Simple Bloom filter implementation for each segment.
  """

  def __init__(self, size, num_hash):
    self.size = size
    self.bits = [0] * size
    self.num_hash = num_hash

  def hash(self, key, i):
    """
    Hash function for key and segment index.
    """
    # Implement your desired hashing function here
    return hash(key) % self.size

  def add(self, key):
    """
    Adds a key to the Bloom filter.
    """
    for i in range(self.num_hash):
      index = self.hash(key, i)
      self.bits[index] = 1

  def query(self, key):
    """
    Checks if a key might be present in the Bloom filter.
    Returns True if all hash functions map to non-zero bits, False otherwise.
    """
    for i in range(self.num_hash):
      index = self.hash(key, i)
      if self.bits[index] == 0:
        return False
    return True

class Segment:
  """
  Represents a single segment with its own Bloom filter and data storage.
  """

  def __init__(self, size, num_hash):
    self.size = size
    self.data = [None] * size
    self.bloom_filter = BloomFilter(size, num_hash)

  def insert(self, key, value):
    """
    Inserts a key-value pair into the segment using selective filter insertion.
    Selects the bucket with the least non-zero Bloom filter bits.
    """
    min_count = self.size
    min_index = None
    for i in range(self.size):
      count = self.bloom_filter.bits[i].count("1")
      if count < min_count:
        min_count = count
        min_index = i

    self.data[min_index] = value
    self.bloom_filter.add(key)

  def search(self, key):
    """
    Searches for a key in the segment using the Bloom filter.
    Returns the value if found, None otherwise.
    """
    if self.bloom_filter.query(key):
      for i in range(self.size):
        if self.data[i] is not None and self.data[i][0] == key:
          return self.data[i][1]
    return None

class SegmentedHashTable:
  """
  Segmented hash table implementation with multiple segments and Bloom filters.
  """

  def __init__(self, num_segments, size_per_segment, num_hash):
    self.segments = [Segment(size_per_segment, num_hash) for _ in range(num_segments)]

  def hash(self, key):
    """
    Hash function to choose the appropriate segment.
    """
    # Implement your desired hashing function here
    return hash(key) % len(self.segments)

  def insert(self, key, value):
    """
    Inserts a key-value pair into the table using selective filter insertion.
    """
    segment = self.segments[self.hash(key)]
    segment.insert(key, (key, value))

  def search(self, key):
    """
    Searches for a key in the table.
    Returns the value if found, None otherwise.
    """
    segment = self.segments[self.hash(key)]
    return segment.search(key)

# Example usage
table = SegmentedHashTable(4, 16, 2)
table.insert("apple", "red")
table.insert("banana", "yellow")
table.insert("orange", "orange")

print(table.search("apple"))  # Output: red
print(table.search("grape"))   # Output: None

# Note: This is a basic implementation and can be further optimized for performance and features.
