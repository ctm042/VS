import math 
import mmh3 
from bitarray import bitarray 

class SegmentedHashTable:
    def __init__(self, N, m, b): #N = number of segments, m = size of segment
        self.N = N #number of segments
        self.m = m #size of segments / number of buckets
        self.b = b #size of buckets
        self.T = [[[None for _ in range(b)] for _ in range(m)] for _ in range(N)]
        self.q = self.largest_prime_below(m)
        self.pseudoInsertFilter = [0 for _ in range(N)]
        self.pseudoBitVector = [0 for _ in range(N)]
        self.bloom = [BloomFilter(b, 0.05) for _ in range(N)]

    
    # Below are my many attempts to implement this abhorent hellspawn. Please take pity on my withered soul.

    # Attempt to translate psuedocode for INSERT from paper to code. FAILED
    # def insert(self, k):
    #     ''' 
    #     Insert a key into the segmented hash table.
    #     k : string
    #         item to be inserted into the segmented hash table 
    #     '''
    #     l = 0                           #set attempts
    #     while not (l == self.m):             #while under the size of each segment
    #         j = self.doubleHash(k, l)                 #get hash index
    #         if self.segmentInsert(k, j, l):     #if inserted into segment succesfully, 
    #             print("inserted key!")
    #             return True                #return
    #         else:
    #             l += 1                  #the hash index in each segment is occupied. next level/index in bucket
    #             print(f"trying next attempt = {l}")

    # def segmentInsert(self, k, j, l): 
    #     ''' 
    #     Scans an index across all segments to insert a key.
    #     k : string
    #         item to be inserted into the segmented hash table 
    #     j : int
    #         attempt
    #     '''
    #     i = 0                                  #set attempts / selected segment
    #     while not (i == self.N):                     #while under the amount of segments
    #         if (self.T[i][j][l] in ['', 'DELETED']):     #if index is available
    #             print(f"found open position at T[{i}][{j}][{l}] because that position = {self.T[i][j][l]}")
    #             self.T[i][j][l] = k                        #store key at position
    #             self.pseudoBitVector[i] += 1    #increment segment count
                
    #             return True                        #done
    #         else:
    #             i += 1                          #else increment attempt
    #     print(f"all positions at {k}'s hashed index {j} are occupied.")
    #     return False                               #no segment has an available position
    

    # # Rewrite attempt. FAILED
    # def insert(self, k):
    #     print("-----------------")
    #     bucketHeight = self.getMinIndex(self.pseudoBitVector)                       #find the first available bucket level
    #     while bucketHeight < len(self.pseudoBitVector):                             #iterate through the rest of the buckets levels
    #         segmentIndex = self.getMinIndex(self.pseudoInsertFilter[bucketHeight])  #find the first smallest segment at that bucket level
    #         for attempts in range(self.m):                                          #attempt to hash
    #             hash = self.doubleHash(k, attempts)                                 #get hash index
    #             print(f"{attempts+1}'th attempt, hash index = {hash}")
    #             valAtHashInd = self.T[segmentIndex][hash][bucketHeight]             #find value at hashed index
    #             print(f"valAtHashInd = {valAtHashInd}")                             #
    #             if (valAtHashInd in [None, 'DELETED']):                               #if hashed index is not occupied
    #                 self.T[segmentIndex][hash][bucketHeight] = k                    #append value to bucket
    #                 print(self.pseudoInsertFilter[segmentIndex][hash][bucketHeight])
    #                 self.pseudoInsertFilter[segmentIndex][hash][bucketHeight] = 1   #update insert filter
    #                 self.updateBitVector(bucketHeight)                              #update bit vector
    #                 print(f"inserted {k} into T[{segmentIndex}][{hash}][{bucketHeight}]")
    #                 return                                                          #successfully return
    #             print(f"T[{segmentIndex}][{hash}][{bucketHeight}] is occupied")
    #         print(f"Could not find a valid hash index, going to next bucket level")
    #         bucketHeight += 1                                                       #no unoccupied index found, raise bucket height 

    # def updateBitVector(self, bucketHeight):
    #     if all(x == 1 for x in self.pseudoInsertFilter[bucketHeight]):
    #         self.pseudoBitVector[bucketHeight] = 1
    #     else:
    #         self.pseudoBitVector[bucketHeight] = 0

    # def getMinIndex(self, values):
    #     return min(range(len(values)), key=values.__getitem__)

    # def checkAvail(self, values):
    #     return False if all(value == 1 for value in values) else True
    

    # Rewrite without the fancy stuff. SUCCESS?
    def insert(self, k):
        bucketHeight = self.getMinIndex(self.pseudoBitVector)                       #find the first available bucket level

        sortedsegs = []                                                     # mimic the effect of the thing? idk
        index_size = list(enumerate(self.pseudoInsertFilter))
        sorted_index_size = sorted(index_size, key=lambda x: x[1])          # who needs comments anyway?
        for index, _ in sorted_index_size:
            sortedsegs.append(index)

        while bucketHeight < len(self.pseudoBitVector):         # tired :(
            for attempts in range(self.m):
                hash = self.doubleHash(k, attempts)
                print(f"\t{k}'s {attempts+1}'th insert attempt. Hash index = {hash}")
                for seg in sortedsegs:
                    # Ideally, this would choose the segment that has an open index without needing to iterate over each segment using a Bit Vector
                    # If two or more segments were to be available, a Selection Filter would be used. i.e. the sector whose Bloom Filter would change the least would be chosen.
                    # This however can cause unbalanced segments, tending to group to already full segments, changing fewer bits than if it were inserted into an empty segment.
                    # There's a fancy solution for this, but all of this is a bit out of scope for the context of this project. Instead, an unoptimal linear solution is used.
                    print(f"\t\tChecking T[{seg}][{hash}][{bucketHeight}] = {self.T[seg][hash][bucketHeight]}")
                    if self.T[seg][hash][bucketHeight] in [None, 'DELETED']:
                        print(f"\t\t\tUnoccupied: Inserting {k} int T[{seg}][{hash}][{bucketHeight}]")
                        self.T[seg][hash][bucketHeight] = k
                        self.bloom[seg].add(k)
                        bucketHeight = self.getMinIndex(self.pseudoBitVector)
                        self.pseudoInsertFilter[seg] += 1
                        return
                    #print("Occupied: Next segment")
                print(f"\tAll segments failed, attempting with new hash attempt")
            print("All attempts failed, next bucket index.")
            bucketHeight += 1
        print("overflow")

    def search(self, k):
        foundSets = []
        for seg in range(len(self.T)):
            # Ideally, this would be search the segment most likely to contain the key, information that would be stored from the Insertion Filter.
            # Instead, we are using an unoptimal linear solution, but maintaining the usage of a Bloom Filter.
            if self.bloom[seg].check(k):
                foundSets.append(seg)
        bucketHeight = 0
        while bucketHeight < len(self.pseudoBitVector):
            for attempts in range(self.m):
                hash = self.doubleHash(k, attempts)
                for seg in foundSets:
                    if self.T[seg][hash][bucketHeight] == k:
                        print(f"found at T[{seg}][{hash}][{bucketHeight}]")
                        return
            bucketHeight += 1

    def delete(self, k):
        foundSets = []
        for seg in range(len(self.T)):
            # Ideally, this would be search the segment most likely to contain the key, information that would be stored from the Insertion Filter.
            # Instead, we are using an unoptimal linear solution, but maintaining the usage of a Bloom Filter.
            if self.bloom[seg].check(k):
                foundSets.append(seg)
        bucketHeight = 0
        while bucketHeight < len(self.pseudoBitVector):
            for attempts in range(self.m):
                hash = self.doubleHash(k, attempts)
                for seg in foundSets:
                    if self.T[seg][hash][bucketHeight] == k:
                        self.T[seg][hash][bucketHeight] = 'DELETED'
                        print(f"found at T[{seg}][{hash}][{bucketHeight}]")
                        return
            bucketHeight += 1


    # Hash function using double hashing
    def doubleHash(self, k, i):
        #print(f"hashing key {k} for the {i+1}th time")
        h1 = hash(k) % self.m            # first hash
        h2 = self.q - hash(k) % self.q        # second hash
        return (h1 + i * h2) % self.m    # double hash function
    
    """HELPER FUNCTIONS"""
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def largest_prime_below(self, size):
        for number in range(size - 1, 1, -1):
            if self.is_prime(number):
                return number

    def printHash(self):
        segind = 0
        for segment in self.T:
            print(f"T{segind} : ")
            b = 0
            for bucket in segment:
                print(f"b{b} = {bucket}")
                b += 1
            segind += 1

class BloomFilter(object): 
  
    ''' 
    Class for Bloom filter, using murmur3 hash function 
    '''
  
    def __init__(self, items_count, fp_prob): 
        ''' 
        items_count : int 
            Number of items expected to be stored in bloom filter 
        fp_prob : float 
            False Positive probability in decimal 
        '''
        # False possible probability in decimal 
        self.fp_prob = fp_prob 
  
        # Size of bit array to use 
        self.size = self.get_size(items_count, fp_prob) 
  
        # number of hash functions to use 
        self.hash_count = self.get_hash_count(self.size, items_count) 
  
        # Bit array of given size 
        self.bit_array = bitarray(self.size) 
  
        # initialize all bits as 0 
        self.bit_array.setall(0) 
  
    def add(self, item): 
        ''' 
        Add an item in the filter 
        '''
        digests = [] 
        for i in range(self.hash_count): 
  
            # create digest for given item. 
            # i work as seed to mmh3.hash() function 
            # With different seed, digest created is different 
            digest = mmh3.hash(item, i) % self.size 
            digests.append(digest) 
  
            # set the bit True in bit_array 
            self.bit_array[digest] = True
  
    def check(self, item): 
        ''' 
        Check for existence of an item in filter 
        '''
        for i in range(self.hash_count): 
            digest = mmh3.hash(item, i) % self.size 
            if self.bit_array[digest] == False: 
  
                # if any of bit is False then,its not present 
                # in filter 
                # else there is probability that it exist 
                return False
        return True
  
    @classmethod
    def get_size(self, n, p): 
        ''' 
        Return the size of bit array(m) to used using 
        following formula 
        m = -(n * lg(p)) / (lg(2)^2) 
        n : int 
            number of items expected to be stored in filter 
        p : float 
            False Positive probability in decimal 
        '''
        m = -(n * math.log(p))/(math.log(2)**2) 
        return int(m) 
  
    @classmethod
    def get_hash_count(self, m, n): 
        ''' 
        Return the hash function(k) to be used using 
        following formula 
        k = (m/n) * lg(2) 
  
        m : int 
            size of bit array 
        n : int 
            number of items expected to be stored in filter 
        '''
        k = (m/n) * math.log(2) 
        return int(k) 




# SegmentedHashTable(N=number of segments >2, m=size of segments >2, b=length of buckets >2)
    
# EXAMPLE 1 - insert - animals
seghash = SegmentedHashTable(4,4,4)
items = ['cat', 'snake', 'dog', 'bird', 'lizard', 'fish', 'beaver', 'ladybug', 
         'squirrel', 'roach', 'ant', 'bear', 'lion', 'tiger', 'panther', 'wolf', 
         'gecko', 'penguin', 'seal', 'shark', 'dolphin', 'turtle', 'sponge', 'kangaroo',
         'ostrich', 'rhino', 'giraffe', 'moose', 'mouse', 'eagle', 'rabbit', 'frog', 
         'elephant', 'koala', 'cheetah', 'chimpanzee', 'peacock', 'octopus', 'flamingo', 'lemur', 
         'platypus', 'armadillo', 'sloth', 'leopard', 'zebra', 'alligator', 'alpaca', 'camel']


# EXAMPLE 2 - insert - abstract
# seghash = SegmentedHashTable(8,8,8)
# input_string = "Hash tables provide efficient table implementations, achieving O(1), query, insert and delete operations at low loads. However, at moderate or high loads collisions are quite frequent, resulting in decreased performance. In this paper, we propose the segmented hash table architecture, which ensures constant time hash operations at high loads with high probability. To achieve this, the hash memory is divided into N logical segments so that each incoming key has N potential storage locations; the destination segment is chosen so as to minimize collisions. In this way, collisions, and the associated probe sequences, are dramatically reduced. In order to keep memory utilization minimized, probabilistic filters are kept on-chip to allow the N segments to be accessed without in-creasing the number of off-chip memory operations. These filters are kept small and accurate with the help of a novel algorithm, called selective filter insertion, which keeps the segments balanced while minimizing false positive rates (i.e., incorrect filter predictions). The performance of our scheme is quantified via analytical modeling and software simulations. Moreover, we discuss efficient implementations that are easily realizable in modern device technologies. The performance benefits are significant: average search cost is reduced by 40% or more, while the likelihood of requiring more than one memory operation per search is reduced by several orders of magnitude."
# items = input_string.split()
# seghash.printHash()


# Leave this uncommented to handle all of the insertions (inserts for both examples)
for item in items:
    seghash.insert(item)
seghash.printHash()

# I mostly focused on insertions so these probably dont have nice debug information. I'm too done to make these look nice.

# EXAMPLE 1B - search
# seghash.search('turtle')
# seghash.printHash()

# EXAMPLE 1C - delete
# seghash.delete('turtle')
# seghash.printHash()




