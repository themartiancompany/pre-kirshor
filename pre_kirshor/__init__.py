#!/usr/bin/env python

from argparse import ArgumentParser as _argument_parser
from os import getcwd
from os.path import join as _path_join
from os.path import realpath
from site import getsitepackages
from .encode import _encode

def _msg_info(
  _msg):
  print(
    f"INFO: {_msg}")

def _dictionary_path_get():
  _site_packages = getsitepackages()[0]
  _share = realpath(
    _path_join(
      _site_packages,
      '..',
      '..',
      '..',
      'share'))

def _extra_words_path_get():
  return _path_join(
    getcwd(),
    "extra-words.txt")

def _text_index_path_get():
  return _path_join(
    getcwd(),
    "text-index.txt")

def _output_path_get():
  return _path_join(
    getcwd(),
    "text-processed.txt")

def _config_show(
  _args):
  if _args.verbose:
    _msg_info(
      f"  target command: {args.target_command}")
    _msg_info(
      f"      input path: {args.input_path}")
    _msg_info(
      f"     output path: {args.output_path}")
    _msg_info(
      f" text words file: {args.text_words_path}")
    _msg_info(
      f"extra words file: {args.extra_words_path}")
    _msg_info(
      f" text index file: {args.text_index_path}")
    _msg_info(
      f" dictionary path: {args.dictionary_path}")

def _main():
  _parser = _argument_parser()
  _arguments = [
    [("target_command", ),
     {"type": str,
      "help": "It can be 'encode' or 'decode'."}],
    [("input_file", ),
     {"type": str,
      "help": 'Text file to process.'}],
    [("--text-words-path", ),
     {'action': "store",
      "type": str,
      "default": '',
      "help": ('Path for the set of the words '
               'in the text (optional).')}],
    [("--extra-words-path", ),
     {'action': "store",
      "type": str,
      "default": _extra_words_path_get(),
      "help": ('Path for the words not present '
               'in the given dictionary.')}],
    [("--text-index-path", ),
     {'action': "store",
      "type": str,
      "default": _text_index_path_get(),
      "help": ('Path for dictionary translation'
               'index for the given text.')}],
    [("--dictionary-path", ),
     {'action': "store",
      "type": str,
      "default": _dictionary_path_get(),
      "help": ('Path of the words dictionary '
               "to use to process the text.")}],
    [("--output-path", ),
     {'action': "store",
      "type": str,
      "default": _output_path_get(),
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
  _config_show()
  if ( _args.target_command == "encode" ):
    _encode_args = (
      _args.input_path,
      _args.output_path,
      _args.text_words_path,
      _args.extra_words_path,
      _args.text_index_path,
      _args.dictionary_path
      )
    _encode(
      *encode_args)

if ( __name__ == "__main__" ):
  _main()
