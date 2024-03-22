# mailcheck

Python wrapper for the MailCheck.ai API

## Installation

```bash
pip install mailcheck
```

## Usage

### Import package

```python
from mailcheck import MailCheckClient
```

### Instantiate client

Without API key:

```python
client = MailCheckClient()
```

With API key (for Pro plan users):

```python
client = MailCheckClient(YOUR_MAILCHECK.AI_API_KEY)
```

### Check domain name

```python
response = client.check_domain('google.com')
print(response)
```

Output:

```bash
{
    'status': 200,
    'domain': 'google.com',
    'mx': True,
    'disposable': False,
    'public_domain': False,
    'did_you_mean': None
}
```

### Check email address

```python
response = client.check_email('bill@microsoft.com')
print(response)
```

Output:

```bash
{
    'status': 200,
    'email': 'bill@microsoft.com',
    'domain': 'microsoft.com',
    'mx': True,
    'disposable': False,
    'public_domain': False,
    'alias': False,
    'did_you_mean': None
}
```
