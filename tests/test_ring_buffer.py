from src.data_structures.ring_buffer import RingBuffer

def test_ring():
    rb = RingBuffer(3)
    rb.push(1); rb.push(2); rb.push(3)
    rb.push(4) # overwrites 1
    assert rb.pop() == 2
    assert rb.pop() == 3
    assert rb.pop() == 4
