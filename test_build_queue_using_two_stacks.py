from build_queue_using_two_stacks import NewQueue


def test_queue_4_items_and_dequeue_2_items():
    q = NewQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    
    i1 = q.dequeue()
    i2= q.dequeue()
    
    assert(i1 == 1)
    assert(i2 == 2)
            