from django.test import TestCase
from django.urls import reverse
from .models import Counter

class CounterViewTests(TestCase):
    def test_counter_creation(self):
        response = self.client.get(reverse('counter:index'))  # Replace 'counter:index' with the correct namespace if needed.
        self.assertEqual(response.status_code, 200)
        counter = Counter.objects.get(key='counter')
        self.assertEqual(counter.value, 1)

