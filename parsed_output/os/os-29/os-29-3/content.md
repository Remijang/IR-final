# 29.3 Concurrent Queues  

As you know by now, there is always a standard method to make a concurrent data structure: add a big lock. For a queue, we’ll skip that approach, assuming you can figure it out.  

Instead, we’ll take a look at a slightly more concurrent queue designed by Michael and Scott [MS98]. The data structures and code used for this queue are found in Figure 29.9 (page 11).  

If you study this code carefully, you’ll notice that there are two locks, one for the head of the queue, and one for the tail. The goal of these two locks is to enable concurrency of enqueue and dequeue operations. In the common case, the enqueue routine will only access the tail lock, and dequeue only the head lock.  

One trick used by Michael and Scott is to add a dummy node (allocated in the queue initialization code); this dummy enables the separation of head and tail operations. Study the code, or better yet, type it in, run it, and measure it, to understand how it works deeply.  

Queues are commonly used in multi-threaded applications. However, the type of queue used here (with just locks) often does not completely meet the needs of such programs. A more fully developed bounded queue, that enables a thread to wait if the queue is either empty or overly full, is the subject of our intense study in the next chapter on condition variables. Watch for it!  

OPERATINGSYSTEMS[VERSION 1.10]  

1 typedef struct node_t {   
2 int value;   
3 struct __node_t \*next;   
4 } node_t;   
5   
6 typedef struct __queue_t {   
7 node_t \*head;   
8 node_t \*tail;   
9 pthread_mutex_t head_lock, tail_lock;   
10 queue_t;   
11   
12 void Queue_Init(queue_t $\star \mathsf { q }$ ) {   
13 node_t \*tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ malloc(sizeof(node_t));   
14 tmp->next $\mathit { \Theta } = \mathrm { ~ N ~ }$ ULL;   
15 q->head $\mathbf { \Sigma } = \mathbf { \Sigma }$ q->tail $\mathbf { \Sigma } = \mathbf { \Sigma }$ tmp;   
16 pthread_mutex_init(&q->head_lock, NULL);   
17 pthread_mutex_init(&q->tail_lock, NULL);   
18 }   
19   
20 void Queue_Enqueue(queue_t $\star \mathsf { q }$ , int value) {   
21 node_t \*tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ malloc(sizeof(node_t));   
22 assert(tmp ! $\mathbf { \Sigma } =$ NULL);   
23 tmp->value $\mathbf { \Sigma } = \mathbf { \Sigma }$ value;   
24 tmp->next $\mathbf { \Sigma } = \mathbf { \Sigma }$ NULL;   
25   
26 pthread_mutex_lock(&q->tail_lock);   
27 q->tail->next $\mathbf { \Sigma } =$ tmp;   
28 q->tail $\mathbf { \Sigma } = \mathbf { \Sigma }$ tmp;   
29 pthread_mutex_unlock(&q->tail_lock);   
30 }   
31   
32 int Queue_Dequeue(queue_t \*q, int \*value) {   
33 pthread_mutex_lock(&q->head_lock);   
34 node_t \*tmp $\mathbf { \Sigma } = \mathbf { \Sigma }$ q->head;   
35 node_t $\star$ new_head $\mathbf { \Sigma } = \mathbf { \Sigma }$ tmp->next;   
36 if (new_head $\scriptstyle = =$ NULL) {   
37 pthread_mutex_unlock(&q->head_lock);   
38 return -1; // queue was empty   
39 }   
40 \*value $\mathbf { \tau } = \mathbf { \tau }$ new_head->value;   
41 q->head $\mathbf { \Sigma } = \mathbf { \Sigma }$ new_head;   
42 pthread_mutex_unlock(&q->head_lock);   
43 free(tmp);   
44 return 0;   
45 }   
1 #define BUCKETS (101)   
2   
3 typedef struct __hash_t {   
4 list_t lists[BUCKETS];   
5 } hash_t;   
6   
7 void Hash_Init(hash_t $^ { \star \mathrm { H } }$ ) {   
8 int i;   
9 for ( $\mathrm { ~ \ : ~ i ~ } = \mathrm { ~ 0 ~ }$ ; i $\prec$ BUCKETS; $\dot { \bf \underline { { 1 } } } + +$ )   
10 List_Init(&H->lists[i]);   
11 }   
12   
13 int Hash_Insert(hash_t $^ { \star \mathrm { H } }$ , int key) {   
14 return List_Insert(&H- $>$ lists[key $\frac { 0 } { 0 }$ BUCKETS], key);   
15 }   
16   
17 int Hash_Lookup(hash_t $^ { \star \mathrm { H } }$ , int key) {   
18 return List_Lookup(&H- $>$ lists[key % BUCKETS], key);   
19 }  

