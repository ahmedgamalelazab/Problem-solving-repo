from singly_linked_list import SinglyLinkedList, Node


linked_list = SinglyLinkedList(10)


linked_list.insert_at_head(20)
linked_list.insert_at_head(30)
linked_list.insert_at_head(40)
linked_list.insert_at_head(50)
linked_list.insert_at_head(60)

# [60,50,40,30,20,10]

# O(N) as runtime and O(1) as space complexity
def find_nth_node_from_end(head: Node, nth: int)-> Node:
    end = head
    result = head
    count = 0
    while count < nth:
        end = end.next
        count = count + 1
    
    while end:
        end = end.next
        result = result.next
    
    return result


def find_nth_node_from_end_recursivly(head, tracker):
    # base case
    if head == None:
        tracker["last_idx"] = 0
        tracker[0] = head # suppose to carry out the None value
        return tracker
    else:
        results = find_nth_node_from_end_recursivly(head.next if head.next else None, tracker)
        if results and "last_idx" in results:
            curr_ctx_idx = results["last_idx"] + 1
            results["last_idx"] = curr_ctx_idx
            results[curr_ctx_idx] = head
            return results
        else:
            raise Exception("results can't be None within the current context")



if __name__ == "__main__":
    # result = find_nth_node_from_end(linked_list.get_head(), 3)
    # result2 = find_nth_node_from_end(linked_list.get_head(), 4)
    # result3 = find_nth_node_from_end(linked_list.get_head(), 5)
    # print(result.data if result.data else None)
    # print(result2.data if result2.data else None)
    # print(result3.data if result3.data else None)
    tracker = {}
    results = find_nth_node_from_end_recursivly(linked_list.get_head(), tracker)
    
    print(tracker[3].data)
    print(tracker[4].data)
    print(tracker[5].data)
