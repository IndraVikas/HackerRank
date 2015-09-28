#include<iostream>
#include<algorithm>
#include <queue>
#include <string>
#include <cstring>

using namespace std;
const int INF = 0x3f3f3f3f;

typedef pair <int, int> pii; 
struct node {
  int x;
  string color;
  int length;
  int parent;
  node *next;
};
 class Dijkstra{
	 public:
	 int N;
	 int M;
	 node **graph;
	 void shortestPath(int start)
	 {
//		 cout << "hello\n";
		 int i = 0;
		 int dist[30002];
		 memset(dist, 0x3f, 30002);
		 dist[start] = 0;
		 std::priority_queue<pii, std::vector<pii>, std::greater<pii> > Q;
		 Q.push(pii(0, start));
		 for(i = 1; i< N+1; i++)
		 {
		 	if(i == start)
			 continue;
			 Q.push(pii(dist[i], i));
		 }
		 while(!Q.empty())
		 {
			 //node
			 int u = Q.top().second;
			 //distance
			 int c = Q.top().first;
			 Q.pop();
			 if (dist[u] < c)
			 continue;
//			 cout << "----------------" << c << "+++++---+++--" << u << "\n";
			 node *temp;
			 temp = graph[u];	 
			 while( temp->next != 0 )
			 {
				 int alt = dist[u] + temp->next->length;
				 int neighbour = temp->next->x;
				 if (alt < dist[neighbour])
				 {
					 dist[neighbour] = alt;
					 Q.push(pii(dist[neighbour], neighbour));
				 }
				 temp  = temp->next;
			 }
		 }
		 i = 1;
		 for (i =1; i < N+1 ; i++)
		 {
			 if(i == start)
			 continue;
			 if  (dist[i] == 1061109567)
			 {
			 cout << -1 <<" ";
			 continue;
			 }
			 cout << dist[i] << " ";
		 }
	 }   
 };
 
 int main() {
	 int N;
	 int M;
	 int T;
	 int j = 0;
	 int length = 0;
	 int source = 0;
	 cin >> T;
	 while(j < T)
	{
	 int i = 1;
	 cin >> N;
	 cin >> M;
	 node  **graph;
	 node **endEdgePointer;
	 graph = new (nothrow) node *[N+1];
	 endEdgePointer = new (nothrow) node *[N+1];
	 while(i<=N)
		 {
			 graph[i] = new node;
			 endEdgePointer[i] = new node;
			 graph[i]->x = i;
//			 graph[i]->length = -1;
			 graph[i]->color = "WHITE";
			 graph[i]->next = 0;
			 endEdgePointer[i] = graph[i];
			 i++;
		 }
	i = 0;
	while(i < M)
		{
//			cout << "hiiiiiiii111111\n";
			int l;
			int r;
			cin >> l;
			cin >> r;
			cin >> length;
			node * temp;
			temp = endEdgePointer[l];
			temp->next = new node;
			temp = temp->next;
			temp->x = r;
			temp->next = 0;
			temp->length = length;
			endEdgePointer[l] = temp;
			temp = endEdgePointer[r];
			temp->next = new node;
			temp = temp->next;
			temp->x = l;
			temp->next = 0;
			temp->length = length;
			endEdgePointer[r] = temp;
			i++;
		}
		cin >> source;
//		cout << "hi2222222222222222222\n";
//	node *temp;
//	 i = 1;
//	 while(i <= N)
//	 {
//	 	temp = graph[i];
//	 	while(temp != 0)
//	 	{
//	 		cout << temp->x << " -- " << temp->length <<"  ";
//	 		temp  = temp->next;
//	 	}
//	 	cout << "\n";
//	 	i++;
//	 }
//	 return(0);
	 Dijkstra djk = Dijkstra();
	 djk.N = N;
	 djk.M = M;
	 djk.graph = graph;
	 djk.shortestPath(source);
	 
	 i = 1;
//	 while(i < N+1)
//		{
//			if(i == start)
//			{
//				i++;
//			 continue;
//			}
//			temp = graph[i];
//			cout << temp->distance << " ";	
//			// cout << "\n";
//			i++;
//		}
//		cout << "\n";
	j++;
	cout << "\n";
	}
 }