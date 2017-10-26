# random-game-name-generator

Python port of the name generator used for https://play.google.com/store/apps/details?id=com.vgname.vgnamegenerator

**Runs on Python 2**

**Not tested in Python 3 yet**

### To run

```sh
git clone https://github.com/enriqueav/random-game-name-generator.git
cd random-game-name-generator
$ python rgng.py
MineElves XIII: Commanders of Witchcraft
$ python rgng.py
The Dragons of Crystals
$ python rgng.py
Eternal Witchcraft
```

### To test

If necessary, install nose2
```sh
pip install nose2
```

To run the test suite:
```sh
nose2 -v
```

For instance:

```sh
$ nose2 -v
test_creation_compound (test_factory.TestTokenFactory) ... ok
test_creation_edition (test_factory.TestTokenFactory) ... ok
test_creation_nonexisting (test_factory.TestTokenFactory) ... ok
test_creation_numeral (test_factory.TestTokenFactory) ... ok
test_creation_random (test_factory.TestTokenFactory) ... ok
test_creation_s1vss2 (test_factory.TestTokenFactory) ... ok
test_creation_subtitle (test_factory.TestTokenFactory) ... ok
test_creation_vthes (test_factory.TestTokenFactory) ... ok
test_generate_name (test_generator.TestNameGenerator) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.045s

OK
```


