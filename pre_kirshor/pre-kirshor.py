
def _compress(
  str _input_path,
  str _output_path):
  _index = open(
    '/usr/share/dict/words',
    'r').read(
      ).split(
        '\n')
  _text = open(
    _input_path,
    'r').read(
      ).split(
        ' ')
  _text_length = len(
    _text)
  _index_length = len(
    _index)
  print(
    f"_text length: {_text_length}")
  _encoded = []
  _found = False
  cdef _i = 0
  cdef _j = 0
  cdef _k = 10
  for _i in range(_text_length):
    if ( _i % 1000 == 0 ):
      print(
        f"reading word {_i}")
    if ( len(_text[_i]) > 3 ):
      for _j in range(_index_length):
        if ( _text[_i] == _index[_j] ):
          _found = True
          break
      if ( _found ):
        _encoded.append(
          f"%{_j}%") 
      else: 
        _encoded.append(
          _text[_i])
    else:
      _encoded.append(
        _text[_i])
  _encoded_string = " ".join(
    _encoded)
  print(
    f"saving to '{_output_path}'")
  open(
    _output_path,
    'w').write(
      _encoded_string)



