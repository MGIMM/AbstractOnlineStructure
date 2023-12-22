# AbstractOnlineStructure

A minimilist abstract structure that handles data-algorithm-loop structure with online learning formalism:

`... -> env -> obs -> agent -> action -> env -> ...`

## usage

check `tests/test_train.py`.

## debug

* built-in pickle  `.save(path)` and `.load(path)` for every object.
* and `.throw(err,  msg)` to handle errors.


