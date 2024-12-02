#!/usr/bin/env python

from .pre_kirshor import _compress
import sys

def _main():
  _input_path = sys.argv[1]
  _output_path = sys.argv[2]
  print(
    f"input file: {_input_path}")
  print(
    f"output file: {_output_path}")
  _compress(
    _input_path,
    _output_path) 

if ( __name__ == "__main__" ):
  _main()
