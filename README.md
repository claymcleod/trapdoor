<p align="center">
  <h1 align="center">
    Trapdoor
  </h1>

  <p align="center">
    <a href="https://github.com/claymcleod/trapdoor/actions/workflows/ci.yml" target="_blank">
      <img alt="Actions: CI Status"
          src="https://github.com/claymcleod/trapdoor/actions/workflows/ci.yml/badge.svg" />
    </a>
    <a href="https://github.com/claymcleod/trapdoor/actions/workflows/docs.yml" target="_blank">
      <img alt="Actions: CI Status"
          src="https://github.com/claymcleod/trapdoor/actions/workflows/docs.yml/badge.svg" />
    </a>
    <a href="https://pypi.org/project/trapdoor/" target="_blank">
      <img alt="PyPI"
          src="https://img.shields.io/pypi/v/trapdoor?color=orange">
    </a>
    <a href="https://pypi.org/project/trapdoor/" target="_blank">
      <img alt="PyPI: Downloads"
          src="https://img.shields.io/pypi/dm/trapdoor?color=orange">
    </a>
    <a href="https://codecov.io/gh/claymcleod/trapdoor" target="_blank">
      <img alt="Code Coverage"
          src="https://codecov.io/gh/claymcleod/trapdoor/branch/main/graph/badge.svg" />
    </a>
    <a href="https://github.com/claymcleod/trapdoor/blob/main/LICENSE.md" target="_blank">
    <img alt="License: MIT"
          src="https://img.shields.io/badge/License-MIT-blue.svg" />
    </a>
  </p>


  <p align="center">
    Turn-key configuration file management for Python packages.
    <br />
    <a href="https://claymcleod.github.io/trapdoor/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/claymcleod/trapdoor/issues/new?assignees=&labels=&template=feature_request.md&title=Descriptive%20Title&labels=enhancement">Request Feature</a>
    ·
    <a href="https://github.com/claymcleod/trapdoor/issues/new?assignees=&labels=&template=bug_report.md&title=Descriptive%20Title&labels=bug">Report Bug</a>
    ·
    ⭐ Consider starring the repo! ⭐
    <br />
  </p>
</p>

## 🎨 Features


* <b>Config Files.</b> Trapdoor makes it easy to create and maintain TOML configuration files.
* <b>Minimal Configuration.</b> Set your store name and start setting and getting keys from the configuration file. Sane defaults are set and useful for most cases.
* <b>Secure Practices.</b> By default, configuration directories are created to be only readable by the user who created them.

## 📚 Getting Started

### Installation

#### Python Package Index

You can also install `trapdoor` using the Python Package Index ([PyPI](https://pypi.org/)).

```bash
pip install trapdoor
```

## 🚌 A Quick Tour

At its foundation, trapdoor is meant to ease the process of creating and maintaining configuration files within your Python tool. Commonly, you will want to use it to create a configuration store, get existing configuration keys, and set configuration keys.

If you're interested in a complete overview of trapdoor's capabilities, please see [**the documentation pages**](https://claymcleod.github.io/trapdoor/)</a>.

```python
# import trapdoor
from trapdoor.trapdoor import Trapdoor

t = Trapdoor('trapdoor-test')           # create a store at ~/.trapdoor-test/config.yml (by default)
t.set('some.nested.key.hello', 'world') # set a key in the configuration file
t.get('some.nested.key.hello')          # get a key from the configuration file
```

For more information, please see [the documentation](https://claymcleod.github.io/trapdoor).

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/claymcleod/trapdoor/issues). Please ensure you fill out the entire template for each of these. You can also take a look at the [contributing guide][contributing-md].

## 📝 License

Copyright © 2021 Clay McLeod. This project is [MIT][license-md] licensed.

[contributing-md]: https://github.com/claymcleod/trapdoor/blob/main/CONTRIBUTING.md
[license-md]: https://github.com/claymcleod/trapdoor/blob/main/LICENSE.md