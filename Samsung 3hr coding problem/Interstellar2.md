# Interstellar 2

The era of the great universe through the us eof wormholes has come. All of the locations in the universe are given as 2-dimensional coordinates of (X,Y). The spacecraft can only move to the parallel directions to the X-axis or Y-axis and it takes 1 second to move 1 distanace. Therefore, the time that the spacecraft needs to move from (x1,y1) to (x2,y2) ia as follows:

```
Time = |x2 - x1| + |y2-y1|
```

There are `N` wormholes in the outerspace. `Ki`, the time to pass through each wormhole, is different for each. The wormhole can be passed through bi-directionally.

*Not all wormholes have to be used to reach the destination point. Also, it is okay if none of the wormholes are used. It is also okay not to use wormhole even though the spacecraft gets to the point of a wormhole.*

Given the starting and destination point (location) of the spacecraft, and the information on each wormholes, find the minimum time from the starting to the destination point.

## Input Format

In the first line, `T`, the number of the test cases is given. From the next lines on, each test case are given. In the first line of each test case,` N`, the number of wormholes is given. In the second line, the starting `[x,y]` and destination` [x,y]` point of the spacecraft are given From the third line to the N+1 line on, each information of wormholes is given. The coordinates `[x,y]` for Gate A and `[x,y]` for Gate B of each wormhole, as well as, the time to pass though the wormhole are given.

## Constraints

1. The number of wormholes, N is greater or equal to 0 and less or equal to 5. (0≤N≤5).
2. The time to pass through a wormhole, Ki, is greater or equal to 0 and less or equal to 3000 (0 ≤ Ki ≤ 3000)
3. X,Y the coordinate of the universe is greater or equal to 0 and less or equal to 1000 (0 ≤ X,Y ≤ 1000)
4. Not in any case are the starting and destination points of the spacecraft, the location of the wormholes the same.
   Output Format

Print "#1" for Test case T, leave a space and print the correct answer. (T means the number of test cases and starts from 1).

## sample input 0

```
5
0
0 0 60 60
1
0 0 2 0
1 0 1 2 0
1
0 0 60 60
40 40 20 20 10
2
100 50 10 5
80 40 10 6 10
80 10 70 40 5
3
500 500 1000 1000
501 501 999 999 1000
1 1 499 499 100
1000 999 0 0 200
```

## Sample output 0

```
#1 120
#2 2
#3 90
#4 41
#5 305
```