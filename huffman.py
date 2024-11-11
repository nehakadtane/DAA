import heapq  # Priority queue implementation

# Node class representing each character and its frequency
class Node:
    def __init__(self, char, freq):
        self.char = char          # Character (or None for internal nodes)
        self.freq = freq          # Frequency of the character
        self.left = None          # Left child in the Huffman Tree
        self.right = None         # Right child in the Huffman Tree

    # Defining comparator operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree and return the root node
def build_huffman_tree(char_freq):
    # Step 1: Create a priority queue of Nodes
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    # Step 2: Build the Huffman Tree
    while len(heap) > 1:
        # Remove two nodes with the smallest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create a new internal node with combined frequency
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        # Add the new node back to the priority queue
        heapq.heappush(heap, merged)

    # Return the root of the Huffman Tree
    return heap[0]

# Function to generate Huffman codes from the Huffman Tree
def generate_huffman_codes(node, code, huffman_code):
    if node is None:
        return

    # If the node is a leaf node, add it to the Huffman code dictionary
    if node.char is not None:
        huffman_code[node.char] = code

    # Traverse the left and right children with updated codes
    generate_huffman_codes(node.left, code + "0", huffman_code)
    generate_huffman_codes(node.right, code + "1", huffman_code)

# Main function to perform Huffman Encoding
def huffman_encoding(char_freq):
    # Step 1: Build Huffman Tree
    root = build_huffman_tree(char_freq)

    # Step 2: Generate Huffman Codes from the Tree
    huffman_code = {}
    generate_huffman_codes(root, "", huffman_code)
    
    return huffman_code

# Example Usage
if __name__ == "__main__":
    # Input: Dictionary of character frequencies
    char_freq = {
        'a': 5,
        'b': 9,
        'c': 12,
        'd': 13,
        'e': 16,
        'f': 45
    }
    
    # Generate Huffman Codes
    huffman_code = huffman_encoding(char_freq)
    
    # Display the Huffman Codes
    print("Character\tHuffman Code")
    for char, code in huffman_code.items():
        print(f"{char}\t\t{code}")
