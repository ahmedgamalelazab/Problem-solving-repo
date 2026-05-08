from singly_linked_list import SinglyLinkedList, Node


linked_list = SinglyLinkedList(10)


linked_list.insert_at_head(20)
linked_list.insert_at_head(30)
linked_list.insert_at_head(40)
linked_list.insert_at_head(50)
linked_list.insert_at_head(60)

# [60,50,40,30,20,10]

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



if __name__ == "__main__":
    result = find_nth_node_from_end(linked_list.get_head(), 3)
    result2 = find_nth_node_from_end(linked_list.get_head(), 4)
    result3 = find_nth_node_from_end(linked_list.get_head(), 5)
    print(result.data if result.data else None)
    print(result2.data if result2.data else None)
    print(result3.data if result3.data else None)
