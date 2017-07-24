### purpose
generating images like this:  

![sample](https://secure.meetupstatic.com/photos/event/2/0/0/c/600_462608204.jpeg)
![another](https://secure.meetupstatic.com/photos/event/b/1/c/c/600_463125516.jpeg)

### stack
Python 3.6, Pillow

### how to use
- install system requirements (`cat system_requirements.txt | xargs apt-get install -y`)
- install python requirements (`pip install -r requirements.txt`)
- create data.yml from meetup.yml (`cp configs/data_example.yml data.yml`)
- `python run.py`

### what can be improved
see [Issues](https://github.com/spbpython/kdpv_generator/issues).
