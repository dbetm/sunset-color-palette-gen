## Setup

**You need to install:**
- [virtualenv](https://virtualenv.pypa.io/en/latest/), please find a tutorial to install on your OS.

**Create virtual env**

`virtualenv venv --python=python3.8`

**Activate virtual env**

`source venv/bin/activate`

**Install dependencies**

`pip install -r exp/requirements.txt`

-------------------

## Usage
**Activate virtual env**

`source venv/bin/activate`


**Add/update dependencies on requirements.txt and install them**

`pip install -r exp/requirements.txt`


**Run tests**
`make testing`


**Deactivate virtual env**

`deactivate`