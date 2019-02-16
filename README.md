# BFS_Large_Database_Search
A simple implementation of BFS (Breadth-first search) for exponentially large database path-finding problems is developed and introduced here. This piece of code is part of an assignment solving **Bacon-Number**-related problems, including finding actors of certain Bacon number, or finding the shortest path, given start and end actor "node". The BFS_Large_Database_Search Method is mainly for the second problem.

- The method requires no external library and any kinds of *import*.
- The method doesn't use `L.pop(0)` and avoid using Lists, which are used widely by other examples but work very slow on a large database.

## Main Concept
The method relies heavily on *sets* and *dictionaries*, using them in almost every possible place. The method introduces two sets: *considered* and *visited* to keep track of considered paths and visited nodes to make the BFS process as efficient as possible.

## File Resources
The main implementation is in **BFS.py** and actor-movie example data was mined from [IMDB](https://www.imdb.com) via the [www.themoviedb.org](https://www.themoviedb.org) API and saved in **Data resources/data.json**. To help reorganize the raw data to the structure the method could work with, a helper function is also saved in the same directory as the main file.

### Related Infomation
1. The mined data example is provided by MIT 6.009.
2. This is my first time organize a public Repository, please feel free to point out mistakes and places to improve.
3. I'm very willing to share and learn, and this little piece of code is distributed under the MIT license.
