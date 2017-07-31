### purpose
generating images like this:  

![sample1](https://secure.meetupstatic.com/photos/event/1/d/b/1/600_463327601.jpeg)
![sample2](https://secure.meetupstatic.com/photos/event/b/1/c/c/600_463125516.jpeg)
![sample3](https://secure.meetupstatic.com/photos/event/8/6/7/b/600_463174427.jpeg)

### stack
Python 3.6, Pillow

### how to use
- install system requirements (`cat system_requirements.txt | xargs apt-get install -y`)
- install python requirements (`pip install -r requirements.txt`)
- create data.yml from meetup.yml (`cp configs/data_example.yml data.yml`)
- `python run.py`

### what can be improved
see [Issues](https://github.com/spbpython/kdpv_generator/issues).
