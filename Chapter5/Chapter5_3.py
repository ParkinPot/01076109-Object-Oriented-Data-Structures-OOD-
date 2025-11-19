class Node:
    def __init__(self, data = None, next = None):
        self.data = data 
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):# insert at end
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def get_last(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr.data
    
    def get_before_last(self):
        itr = self.head
        while itr.next and itr.next.next:
             itr = itr.next
        return itr.data
    
    def get_commits(self):
        commits = []
        itr = self.head
        while itr:
            commits.append(itr.data)
            itr = itr.next
        return commits
    
input = input("Git History: ").split('|')
branch_commit = []
# commit = a single commit
# commits = one branch's list of commits
for branch in input:# new linked list for each branch
    commits = [commit.strip() for commit in branch.strip().split('->')]
    branch_list = LinkedList()

    for commit in commits:
        branch_list.append(commit)

    branch_commit.append(branch_list)

common_parent = branch_commit[0].get_last()

all_same = True
for i in range(1, len(branch_commit)):
    if branch_commit[i].get_last() != common_parent:
        all_same = False
        break
        
if all_same:
    print("Are these branches in the same repository? True")

    commit_sets = [branch.get_commits() for branch in branch_commit]# a list where each element is a list of commits(list of branch)

    before_parent = [branch.get_before_last() for branch in branch_commit]# a list of second last element before parent

    shared_commits = []# shared commits that appear in mutliple branch

    merge_count = 0

    for i in range(len(commit_sets)):# first branch
        for j in range(i + 1, len(commit_sets)):# second branch
            # check if these two branches share any commits (excluding common parent)
            has_shared_commit = False
            for commit in commit_sets[i]:
                if commit != common_parent and commit not in before_parent and commit in commit_sets[j] and commit not in shared_commits:
                    shared_commits.append(commit)
                    has_shared_commit = True
                    
            # commits that appear in multiple branch
            if has_shared_commit:
                merge_count += 1
    
    print(f"{merge_count} Merge(s)")
    # print(shared_commits)
    # print(before_parent)
else:
    print("Are these branches in the same repository? False")
    





    