# PYTHON IP CHECKER      

**ip_checker** *is a python library which you can use to validate ip address and check whether an ip is private or public*
*& you can easily implement this library easily on your api, app or ...*

##### This library works on both python2 & python 3

* Usage:
``` python
 >>> from ip_checker import ip_checker
 >>> ip_obj = ip_checker('123.111.23.1')
 >>> ip_obj.is_valid()
 >>> True
 >>> ip_obj.is_public()
 >>> True
 >>> ip_obj.is_private()
 >>> False
 ```

* Running Test
``` shell
python -m unittest test
```

## Contributions

Feel free to create issues / pull requests.

## License

```
The MIT License (MIT)

Python IP Address Checker library
Copyright (c) 2018 Bisrat Yalew (http://github.com/bisratyalew).

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

#### Thanks!