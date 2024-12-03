def _read_text_as_list(
  str _path,
  str _separator):
  return open(
    _path,
    'r',
    encoding='utf8').read(
      ).split(
        _separator)

def _save_list_as_text(
  list _list,
  str _list_type,
  str _separator,
  str _path,
  str _msg):
  cdef str _string
  print(
    f"INFO: {_msg}")
  if ( _list_type == "int" ):
    _string = _separator.join(
      map(
        str,
        _list))
  elif ( _list_type == "str" ):
    _string = _separator.join(
      _list)
  f = open(
    _path,
    'w',
    encoding='utf8').write(
      _string)
  f.close()

def _text_index_save(
  list _text_index,
  str _text_index_path):
  _save_list_as_text(
    _text_index,
    "int",
    " ",
    _text_index_path,
    f"saving numerical index to '{_text_index_path}'")

def _text_words_save(
  list _text_words,
  str _text_words_path):
  _save_list_as_text(
    _text_words,
    "str",
    " ",
    _text_words_path,
    f"saving words set to '{_text_words_path}'")

def _extra_words_save(
  list _extra_words,
  str _extra_words_path):
  _save_list_as_text(
    _extra_words,
    "str",
    " ",
    _extra_words_path,
    f"saving not indexed words to '{_extra_words_path}'")

def _encoded_text_save(
  list _encoded_text,
  str _encoded_text_path):
  _save_list_as_text(
    _encoded_text,
    "str",
    " ",
    _encoded_text_path,
    f"saving encoded text to '{_encoded_text_path}'")

def _index_build(
  str _dictionary_path,
  list _text_words,
  int _text_words_length):
  cdef list _index = []
  cdef list _extra_words = []
  cdef list _dictionary
  cdef int _dictionary_length
  cdef int _word = 0
  cdef int _word_length
  cdef int _term = 0
  cdef int _word_new = -1
  cdef bint _found
  _dictionary = _read_text_as_list(
    _dictionary_path,
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
            _word_new)
        _word_new = _word_new - 1
        _extra_words.append(
          _text_words[_word])
    else:
      _index.append(
        _word_new)
      _word_new = _word_new - 1
      _extra_words.append(
        _text_words[_word])
  return _index, _extra_words

def _encode(
  str _text_path,
  str _encoded_text_path,
  str _text_words_path,
  str _text_index_path,
  str _extra_words_path,
  str _dictionary_path):
  cdef _word = 0
  cdef _term = 0
  cdef list _text
  cdef int _text_length
  cdef list _text_words
  cdef set _text_words_set
  cdef int _text_words_length
  cdef list _text_index
  cdef str _text_index_string
  cdef list _extra_words
  cdef str _extra_words_string
  cdef list _encoded_text = []
  cdef str _encoded_string
  if ( _dictionary_path == "" ):
    _dictionary_path = '/usr/share/dict/words'
  _text = _read_text_as_list(
    _text_path,
    ' ')
  _text_length = len(
    _text)
  print(
    f"INFO: text is long {_text_length} words")
  _text_words_set = set(
    _text)
  _text_words_set.remove(
    '')
  _text_words_length = len(
    _text_words_set)
  print(
    f"INFO: words contains {_text_words_length} distinct words")
  _text_words = list(
    _text_words_set)
  del _text_words_set
  if ( _text_words_path != "" ):
    _text_words_save(
      _text_words,
      _text_words_path)
  _text_index, _extra_words = _index_build(
    _dictionary_path,
    _text_words,
    _text_words_length)
  _text_index_save(
    _text_index,
    _text_index_path)
  _extra_words_save(
    _extra_words,
    _extra_words_path)
  for _word in range(_text_length):
    _translated = False
    if ( _word % 1000 == 0 ):
      print(
        f"INFO: encoding word {_word} out of {_text_length}")
    for _term in range(_text_words_length):
      if ( _text[_word] == _text_words[_term] ):
        _encoded_text.append(
          f"%{_term}%") 
        break
  _encoded_text_save(
    _encoded_text,
    _encoded_text_path)
