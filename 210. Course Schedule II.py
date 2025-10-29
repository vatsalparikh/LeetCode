class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        visiting = set()
        visited = set()
        self.toporder = []

        for course in range(numCourses):
            if not self.dfs(graph, course, visiting, visited):
                return []
        
        return self.toporder[::-1]

    def dfs(self, graph, course, visiting, visited):
        if course in visiting:
            return False

        if course in visited:
            return True

        visiting.add(course)

        for neighbor in graph[course]:
            if not self.dfs(graph, neighbor, visiting, visited):
                return False
        
        visited.add(course)
        self.toporder.append(course)
        visiting.remove(course)

        return True