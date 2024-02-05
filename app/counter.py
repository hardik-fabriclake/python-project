To update the code in "app/counter.py" to allow for incrementing and decrementing values by 5, and to create a new endpoint, you can modify the code as follows:

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, num=1):
        self.value += num
        return self.value

    def decrement(self, num=1):
        if self.value >= num:
            self.value -= num
        return self.value

    def reset(self):
        self.value = 0
        return self.value
```

In this updated code, the `increment` and `decrement` methods now accept an optional parameter `num` which defaults to 1. This parameter allows you to specify the amount by which the value should be incremented or decremented. The `increment` method increments the value by `num` and the `decrement` method decrements the value by `num` as long as the value is greater than or equal to `num`. The functions return the updated value.

To create a new endpoint, you'll need to modify the API code that handles the requests. Without seeing the complete API code, it's difficult to provide an exact solution, but you can start by adding a new route in your API framework where you'll handle the new operations. Here's a generic example using Flask:

```python
from flask import Flask, request

app = Flask(__name__)
counter = Counter()

@app.route('/increment_by_five', methods=['POST'])
def increment_by_five():
    num = 5
    if 'num' in request.json:
        num = request.json['num']

    value = counter.increment(num)
    return {'value': value}

@app.route('/decrement_by_five', methods=['POST'])
def decrement_by_five():
    num = 5
    if 'num' in request.json:
        num = request.json['num']

    value = counter.decrement(num)
    return {'value': value}

if __name__ == '__main__':
    app.run()
```

In this example, we define two new endpoints: `/increment_by_five` and `/decrement_by_five`, both accepting POST requests. Each endpoint checks if there is a 'num' parameter in the JSON payload of the request. If present, it uses the provided value to increment or decrement by. Otherwise, it defaults to incrementing or decrementing by 5. The updated value is returned as a JSON response.

Please note that the exact implementation will depend on the framework and structure of your existing API.