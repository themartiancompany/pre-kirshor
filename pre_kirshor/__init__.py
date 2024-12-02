#!/usr/bin/env python

from .pre_kirshor import _compress
import sys

def _main():
  _input_path = sys.argv[1]
  _output_path = sys.argv[2]
  _text_words_path = sys.argv[3]
  _text_index_path = sys.argv[4]
  _dictionary_path = sys.argv[5]
  print(
    f"input file: {_input_path}")
  print(
    f"output file: {_output_path}")
  print(
    f"text words file: {_text_words_path}")
  print(
    f"text index file: {_text_index_path}")
  print(
    f"dictionary file: {_dictionary_path}")
  _compress(
    _input_path,
    _output_path,
    _text_words_path,
    _text_index_path,
    _dictionary_path
    ) 

if ( __name__ == "__main__" ):
  _main()
