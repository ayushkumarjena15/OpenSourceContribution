from src.data_structures.priority_queue import PriorityQueue

def test_pq():
    pq = PriorityQueue()
    pq.push('low', 10)
    pq.push('high', 1)
    assert pq.pop() == 'high'
    assert pq.pop() == 'low'
