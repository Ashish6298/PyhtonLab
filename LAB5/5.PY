import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")
def encode_text(text, huffman_tree):
    encoding_map = {}

    def traverse_tree(node, code=''):
        if node.left:
            traverse_tree(node.left, code + '0')
        if node.right:
            traverse_tree(node.right, code + '1')
        if not node.left and not node.right:
            encoding_map[node.symbol] = code

    traverse_tree(huffman_tree)

    encoded_text = ''
    for char in text:
        encoded_text += encoding_map[char]

    return encoded_text

def decode_text(encoded_text, huffman_tree):
    decoded_text = ''
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if not current_node.left and not current_node.right:
            decoded_text += current_node.symbol
            current_node = huffman_tree

    return decoded_text

chars = input("Enter characters: ").split(' ')
freq = [int(i) for i in input("Enter frequencies: ").split(' ')]

nodes = []

for x in range(len(chars)):
    heapq.heappush(nodes, Node(freq[x], chars[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = '0'
    right.huff = '1'
    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, new_node)
printNodes(nodes[0])

huffman_tree = nodes[0]

encoded_text = input("Enter the encoded text: ")
decoded_text = decode_text(encoded_text, huffman_tree)
print("Decoded text:", decoded_text)
text_input = input("Enter text to encode: ")
encoded_binary_text = encode_text(text_input, huffman_tree)
print("Encoded binary text:", encoded_binary_text)