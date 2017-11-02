[![Build Status](https://travis-ci.org/spbpython/kdpv_generator.svg?branch=master)](https://travis-ci.org/spbpython/kdpv_generator)

### purpose
generating images like this:  

![sample1](https://secure.meetupstatic.com/photos/event/1/d/b/1/600_463327601.jpeg)
![sample2](https://secure.meetupstatic.com/photos/event/b/1/c/c/600_463125516.jpeg)
![sample3](https://secure.meetupstatic.com/photos/event/8/6/7/b/600_463174427.jpeg)

### features
- draw your image declarative way!
- cyrillic support
- custom fonts (ttf, otf) support
- use local or remote image files
- auto-crop image file to round form

### stack
Python 3.5/3.6 (<3.5 is not supported due to use of `typing` module.), Pillow

### how to use
- install system requirements (`cat system_requirements.txt | xargs apt-get install -y`)
- install python requirements (`pip install -r requirements.txt`)
- create data.yml from any of existing configs (for example, `cp kdpv_generator/configs/meetup.yml data.yml`)
- `python run.py`

### tests
the pytest is used for the tests.  
to run the tests use command:  
`python3 -m pytest kdpv_generator`

### what can be improved
see [Issues](https://github.com/spbpython/kdpv_generator/issues).
