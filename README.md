# IsCacheable

iscacheable is simple tool to determine if a URL is cacheable or not. It
both prints whether the URL is cacheable to stdout and exits with 0 or 1
if the URL is cacheable or not, respectively.

Once installed, `iscacheable` is available as a command.


### Usage

To use, provide `iscacheable` the URL to test and let it go to
work. `iscacheable` will then:

  1. Send an HTTP `HEAD` request to the URL.
  2. Fetch the response headers.
  3. Test if the response headers are cacheable.
  4. Print `Cacheable.` if the URL is cacheable, `Not cacheable.` otherwise.
  5. Exit with exit code 0 if URL is cacheable, 1 otherwise.

Example:

```
$ iscacheable https://www.google.com
Not cacheable.
$ echo $?
1

$ iscacheable https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png
Cacheable.
$ echo $?
0
```

Of course iscacheable can also be used programmatically, too.

```python
>>> from iscacheable import determineCacheability
>>>
>>> determineCacheability('https://www.google.com')
False
>>> determineCacheability('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
True
```

That's it. Simple.


### Installation

Installing iscacheable with pip is easy.

```
$ pip install iscacheable
```