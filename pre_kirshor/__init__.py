#!/usr/bin/env python

from argparse import ArgumentParser as _argument_parser
from os.path import join as path_join
from os.path import realpath
from site import getsitepackages
from .compress import _compress

def _dictionary_path_get():
  _site_packages = getsitepackages()[0]
  _share = realpath(
    path_join(
      _site_packages,
      '..',
      '..',
      '..',
      'share'))

def _main():
  _parser = _argument_parser()
  _arguments = [
    [("input_file", ),
     {"type": str,
      "help": 'text file to pre-process.'}],
    [("--key", ),
     {'action': "store",
      "type": str,
      "default": _key_path_get(),
      "help": ('absolute path of api key '
               'of an etherscan/blockscout-like service.')}],
    [("--network", ),
     {'action': "store",
      "type": str,
      "default": 'main',
      "help": ('network to connect to '
               '(eth, bsc, avax, polygon, '
               'optimism, base, arbitrum, '
               'fantom, taiko, snowscan, '
               'gnosis, kcc, ethw, etc, '
               'doge, polygonzk, one)')}],
    [("--dictionary-path", ),
     {'action': "store",
      "type": str,
      "default": _dictionary_path_get(),
      "help": ('path of the words dictionary '
               "to use to process the text.")}],
    [("--output-file", ),
     {'action': "store",
      "type": str,
      "default": 'processed.txt',
      "help": 'path of resulting processed file.'}],
    [("--verbose", ),
     {'dest': "verbose",
      'action': "store_true",
      "default": False,
      "help": 'extended output'}]
  ]
  for _argument in _arguments:
      _args, _kwargs = _argument
      _parser.add_argument(
        *_args,
        **_kwargs)
  _args = _parser.parse_args()
  _abi_get_args = (
    _args.contract_address,
    _args.network,
    _args.blockchain,
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
