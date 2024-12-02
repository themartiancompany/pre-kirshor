def _index_get(
  str _dictionary_path,
  list _text_words,
  int _text_words_length):
  cdef list _index = [];
  cdef list _dictionary
  cdef int _dictionary_length
  cdef int _word = 0
  cdef int _word_length
  cdef int _term = 0
  cdef int _none = -1
  cdef bint _found
  _dictionary = open(
    _dictionary_path,
    'r').read(
      ).split(
        '\n')
  _dictionary_length = len(
    _dictionary)
  print(
    f"INFO: dictionary size: {_dictionary_length}")
  for _word in range(
    _text_words_length):
    if ( _word % 1000 == 0 ):
      print(
        f"INFO: indexing word {_word}")
    _word_length = len(
      _text_words[_word])
    if ( _word_length > 3 ):
      _found = False
      for _term in range(
        _text_words_length):
        if ( _text_words[_word] == _dictionary[_term] ):
          _index.append(
            _term)
          _found = True
          break
      if ( _found == False ):
        _index.append(
            _none)
    else:
      _index.append(
        _none)
  return _index

def _compress(
  str _input_path,
  str _output_path,
  str _text_words_path,
  str _text_index_path,
  str _dictionary_path):
  cdef _word = 0
  cdef _term = 0
  cdef list _text
  cdef int _text_length
  cdef list _text_words
  cdef set _text_words_set
  cdef int _text_words_length
  cdef list _text_index
  cdef list _encoded = []
  cdef str _encoded_text
  if ( _dictionary_path == "" ):
    _dictionary_path = '/usr/share/dict/words'
  _text = open(
    _input_path,
    'r').read(
      ).split(
        ' ')
  _text_length = len(
    _text)
  print(
    f"INFO: text is long {_text_length} words")
  _text_words_set = set(
    _text)
  _text_words_length = len(
    _text_words_set)
  print(
    f"INFO: words contains {_text_words_length} distinct words")
  _text_words = list(
    _text_words_set)
  print(
    f"saving words set to '{_text_words_path}'")
  open(
    _text_words_path,
    'w').write(
      _text_words)
  del _text_words_set
  _text_index = _index_get(
    _dictionary_path,
    _text_words,
    _text_words_length)
  print(
    f"saving numerical index to '{_text_index_path}'")
  open(
    _text_index_path,
    'w').write(
      _text_index)
  for _word in range(_text_length):
    _translated = False
    if ( _word % 1000 == 0 ):
      print(
        f"INFO: translating word {_word}")
    for _term in range(_text_words_length):
      if ( _text[_word] == _text_words[_term] ):
        _encoded.append(
          f"%{_term}%") 
        break
  _encoded_text = " ".join(
    _encoded)
  print(
    f"saving encoded text to '{_output_path}'")
  open(
    _output_path,
    'w').write(
      _encoded_text)

