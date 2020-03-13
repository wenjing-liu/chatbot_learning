import sys
import struct
import math
import numpy as np

max_w = 50
float_size = 4

def load_vectors(input):
  print('begin load vectors')

  with open(input, 'rb') as input_file:
    words_and_size = input_file.readline().strip()
    words = long(words_and_size.split(' ')[0])
    size = long(words_and_size.split(' ')[1])
    print('words =', words)
    print('size = ', size)

    word_vector = {}

    for b in range(0, words):
      a = 0
      word = ''
      while True:
        c = input_file.read(1)
        word = word + c
        if False == c or c == ' ':
          break
        if a < max_w and c != '\n':
          a = a + 1
      word = word.strip()

      vector = np.empty([200])
      for index in range(0, szie):
        m = input_file.read(float_size)
        (weight,) = struct.unpack('f', m)
        vector[index] = weight

      word_vector[word.decode('utf-8')] = vector

  print('load vector finish')
  return word_vector


if __name__ == '__main__':
  if 2 != len(sys.argv):
    print("Usage: ", sys.argv[0], "vectors.bin")
    sys.exit(-1)
  d = load_vectors(sys.argv[1])
  print(d[u'真的'])

