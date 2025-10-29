class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        visiting = set()
        visited = set()

        for course in range(numCourses):
            if not self.dfs(graph, course, visiting, visited):
                return False
        
        return True

    def dfs(self, graph, course, visiting, visited):
        if course in visiting:
            return False
        if course in visited:
            return True

        visiting.add(course)
        visited.add(course)

        for neighbor in graph[course]:
            if not self.dfs(graph, neighbor, visiting, visited):
                visiting.remove(course)
                return False
        
        visiting.remove(course)
        return True