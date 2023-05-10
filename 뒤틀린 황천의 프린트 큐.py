t = int(input())
for ___ in range(t):
    temporary = 0
    temporary3 = 0
    document_priority3 = []
    n, pos = map(int, input().split())
    document_priority = list(map(int, input().split()))
    document_priority2 = document_priority[:]

    for _ in range(n):
        document_priority3.append(_)
    a = document_priority3[pos] # 원본 위치기억

    for qwe in range(n):
        while not document_priority2[0] == max(document_priority2):
            temporary2 = document_priority2[0]
            document_priority2.pop(0)
            document_priority2.append(temporary2)

            temporary3 = document_priority3[0]
            document_priority3.pop(0)
            document_priority3.append(temporary3)
        if document_priority2[0] == document_priority[pos]:
            print(document_priority3.index(a))
            break
        else:
            document_priority2.pop(0)
            continue
